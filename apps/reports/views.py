from datetime import datetime, time
from decimal import Decimal

from django.db.models import Sum
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets # status
from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.models import CommonInfo, EmployeeWorkBlock, ServiceTicket
from apps.authentication.models import Mechanic, User
from apps.authentication.permissions import IsAuthenticated

from auditlog.models import LogEntry
from apps.time_tracker.models import IndirectHours
from .filters import ReportsByUsersHoursFilter, ServiceTicketFullFilter, UserFilter
from .permissions import HasAccessToReports
from .serializers import (ReportsByUsersSerializer,
                          ReportsByServiceTicketsSerializer,
                          DetailedReportByMechanicSerializer,
                          IndirectHoursReportSerializer)

import csv
import json

class ReportsABCViewSet(ListModelMixin,
                        viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated, HasAccessToReports,)
    pagination_class = None


class ReportsByUsersViewSet(ReportsABCViewSet):
    """
    list:

    ReportsByUsers endpoint.\n
        Note: User roles are constants:
            {
                1: "Admin",
                2: "Biller",
                3: "Manager",
                4: "Mechanic"
            }\n
        Filter example: /?role=Mechanic&status=Archived&ordering=-last_name
        Available ordering fields: email, first_name, last_name, role
    """

    queryset = User.objects.all().order_by('-id')
    #for query in queryset:
    #    print("queryset:  ", query)
    filterset_class = UserFilter
    serializer_class = ReportsByUsersSerializer


class ReportsByServiceTicketsViewSet(ReportsABCViewSet):
    """
    list:

    ReportsByServiceTickets endpoint.\n
    Required parameters: start_date, end_date\n
    \n
    Filter example: ?start_date=01/01/2020&end_date=03/31/2020&ordering=-id
    Available ordering fields: id, status, date, number, created_by, requested_by, approved_by,
        location, customer, submitted_for_approval_timestamp, approved_timestamp
    """

    queryset = ServiceTicket.objects.filter(is_archive=False).\
        select_related('connected_job__customer', 'created_by', 'requester', 'approval', 'connected_job__location').\
        prefetch_related('employee_works__employee', 'connected_job__managers', 'connected_job__mechanics').\
        select_related('connected_job__created_by')
    filterset_class = ServiceTicketFullFilter
    serializer_class = ReportsByServiceTicketsSerializer


class ReportsByIndirectHoursViewSet(ReportsABCViewSet):

    queryset = IndirectHours.objects.filter(status=3, is_archive=False).select_related('time_code').prefetch_related('mechanic')
    filterset_class = ReportsByUsersHoursFilter
    serializer_class = IndirectHoursReportSerializer


class ReportsByUsersHoursViewSet(ReportsABCViewSet):
    """
    list:

    Payroll reports endpoint.\n
        Filter example: /?start_date=09/13/2019&end_date=10/13/2020&ordering=-sum
        Available ordering fields: first_name, last_name, sum
    """

    queryset = IndirectHours.objects.filter(status=IndirectHours.APPROVED, is_archive=False).order_by('-id')
    filterset_class = ReportsByUsersHoursFilter
    swagger_schema = None

    def sort(self, data, order_by):
        if order_by == 'sum':
            return sorted(data, key=lambda item: item['sum'])
        elif order_by == '-sum':
            return sorted(data, key=lambda item: item['sum'], reverse=True)
        elif order_by == 'first_name':
            return sorted(data, key=lambda item: item['hours'][0]['first_name'])
        elif order_by == '-first_name':
            return sorted(data, key=lambda item: item['hours'][0]['first_name'], reverse=True)
        elif order_by == 'last_name':
            return sorted(data, key=lambda item: item['hours'][0]['last_name'])
        elif order_by == '-last_name':
            return sorted(data, key=lambda item: item['hours'][0]['last_name'], reverse=True)
        return data

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        start_date = datetime.strptime(
            request.query_params.get('start_date'), settings.DATE_FORMAT
        )
        end_date = datetime.strptime(request.query_params.get('end_date'), settings.DATE_FORMAT)
        # TODO: Optimize everything

        unique_indirect_hour_mechanics = tuple(
            qs.order_by('mechanic').distinct('mechanic').values_list('mechanic', flat=True)
        )
        unique_employee_work_mechanics = tuple(EmployeeWorkBlock.objects.filter(
            service_ticket__status=CommonInfo.APPROVED,
            service_ticket__date__gte=start_date,
            service_ticket__date__lte=end_date,
            service_ticket__is_archive=False,
            start_time__isnull=False,
            end_time__isnull=False
        ).order_by('employee').distinct('employee').values_list('employee', flat=True))
        mechanics = set(unique_indirect_hour_mechanics + unique_employee_work_mechanics)
        data = []
        for mechanic_id in mechanics:
            mechanic = Mechanic.objects.get(id=mechanic_id)
            mechanic_indirect_hours_qs = qs.filter(mechanic=mechanic)

            # unique indirect hours per mechanic
            indirect_hours = mechanic.get_unique_indirect_hours(mechanic_indirect_hours_qs)
            indirect_hours = [{
                'time_code': time_code,
                'hours': hours,
                'first_name': mechanic.first_name,
                'last_name': mechanic.last_name
            } for time_code, hours in indirect_hours.items()]

            # total working time per mechanic
            total_working_time = mechanic.get_total_working_time(
                start_date=start_date, end_date=end_date
            )
            indirect_hours.insert(0, {  # Move it to beggining of the list
                'time_code': 'REG',  # TODO: Rename it
                'hours': total_working_time,
                'first_name': mechanic.first_name,
                'last_name': mechanic.last_name
            })

            # total hours per mechanic
            total_indirect = mechanic_indirect_hours_qs.aggregate(
                Sum('hours')
            ).get('hours__sum') or 0
            sum = Decimal(Decimal(total_working_time) + Decimal(total_indirect)).quantize(Decimal('.01'))

            data.append({'sum': sum, 'hours': indirect_hours})
        data = self.sort(data, request.query_params.get('ordering'))
        return Response(data)


class DetailedReportByMechanicViewSet(ReportsABCViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = Mechanic.objects.all()
    serializer_class = DetailedReportByMechanicSerializer

    report_status = None

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_mechanic:
            user_id = user.id
        elif user.is_admin or user.is_superuser or user.is_manager:
            user_id = self.request.query_params.get('user_id')
        qs = queryset.filter(pk=user_id)
        return qs

    def list(self, request, *args, **kwargs):
        start_date, end_date = self.__validate_request(request)
        instance = self.get_object()

        mechanic_service_tickets_hours_qs = ServiceTicket.objects.filter(
            employee_works__employee=instance,
            date__gte=start_date,
            date__lte=end_date
        ).distinct()

        mechanic_indirect_hours_qs = IndirectHours.objects.filter(
            mechanic=instance,
            date__gte=start_date,
            date__lte=end_date,
            is_archive=False
        )

        if self.report_status is not None:
            mechanic_indirect_hours_qs = mechanic_indirect_hours_qs.filter(status=self.report_status)
            mechanic_service_tickets_hours_qs = mechanic_service_tickets_hours_qs.filter(status=self.report_status+1)

        serializer = self.get_serializer(
            instance,
            mechanic_service_tickets_hours_qs=mechanic_service_tickets_hours_qs,
            mechanic_indirect_hours_qs=mechanic_indirect_hours_qs
        )
        return Response(serializer.data)

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        obj = self.filter_queryset(self.get_queryset()).first()

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def __validate_request(self, request):
        if request.query_params.get('user_id'):
            try:
                int(request.query_params.get('user_id'))
            except ValueError:
                raise ValidationError(
                    {'user_id': _("You should provide int value for user_id")}
                )
        elif request.user.is_mechanic:
            pass
        else:
            raise ValidationError(
                {'user_id': _("You should pass user_id if you logged as admin")}
            )

        if request.query_params.get('status'):
            if request.query_params.get('status') == 'rejected':
                self.report_status = 2
            elif request.query_params.get('status') == 'pending for approval':
                self.report_status = 1
            elif request.query_params.get('status') == 'approved':
                self.report_status = 3
            elif request.query_params.get('status') == 'open':
                self.report_status = 0
            else:
                raise ValidationError({'status': 'You have provided invalid status for the search!'})

        if request.query_params.get('start_date'):
            try:
                start_date = datetime.strptime(
                    request.query_params.get('start_date'), settings.DATE_FORMAT
                )
            except ValueError as e:
                raise ValidationError({'start_date': e})
        else:
            raise ValidationError({'start_date': _("You should pass start_date")})

        if request.query_params.get('end_date'):
            try:
                end_date = datetime.strptime(
                    request.query_params.get('end_date'), settings.DATE_FORMAT
                )
            except ValueError as e:
                raise ValidationError({'end_date': e})
        else:
            raise ValidationError({'end_date': _("You should pass end_date")})

        if start_date > end_date:
            raise ValidationError(
                {'start_date': _("The start_date can't be ahead of the end_date")}
            )

        return start_date, end_date

def status_code_to_text(status_code):
    """
    Convert status code to text representation.
    """
    if status_code == '1':
        return 'Submitted'
    elif status_code == '2':
        return 'Rejected'
    elif status_code == '3':
        return 'Approved'


class ServiceTicketChangelog(APIView):

    permission_classes = (IsAuthenticated, HasAccessToReports)

    def post(self, request):
        return Response({'error': 'Method not allowed',}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get(self, request):
        start_date = datetime.combine(datetime.strptime(request.query_params.get('start_date'), "%m/%d/%Y"), time.min)
        end_date = datetime.combine(datetime.strptime(request.query_params.get('end_date'), "%m/%d/%Y"), time.max)
        log_entries = list(LogEntry.objects.get_for_model(ServiceTicket).filter(timestamp__gte=start_date,
                                                                                timestamp__lte=end_date))
        indirect_Hours_log = list(LogEntry.objects.get_for_model(IndirectHours).filter(timestamp__gte=start_date,
                                                                                timestamp__lte=end_date))
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="ST-log.csv"'
        csv_writer = csv.writer(response)
        csv_writer.writerow(['Time', 'Task ID', 'User', 'IP Address', 'Change'])
        for e in log_entries:
            csv_writer.writerow([e.timestamp.strftime("%m/%d/%Y %H:%M"), 'Service Ticket Id #{}'.format(e.object_id), e.actor, e.remote_addr,
                                 e.changes])
        for e in indirect_Hours_log:
            changes_dict = json.loads(e.changes)
            
            # Preprocess the changes data
            if 'status' in changes_dict:
                changes_dict['status'] = [status_code_to_text(code) for code in changes_dict['status']]
            
            changes = json.dumps(changes_dict)            
            csv_writer.writerow([e.timestamp.strftime("%m/%d/%Y %H:%M"), 'Indirect Hours Id #{}'.format(e.object_id), e.actor, e.remote_addr,
                         changes])
        return response
