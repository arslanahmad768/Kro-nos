from django.utils.translation import gettext_lazy as _

import rest_framework_filters as filters
from rest_framework.exceptions import ValidationError

from apps.api.models import ServiceTicket
from apps.authentication.filters import UserFilter
from apps.authentication.models import User
from apps.time_tracker.models import IndirectHours

from django.db.models import Q

class DateRangeFilterMixin:
    """
    Validate start_date and end_date query parameters are required.
    Validate start_date cannot be more than end_date.
    """

    @property
    def qs(self):
        if hasattr(self, '_qs'):
           return self._qs

        start_date = self.form.cleaned_data.get('start_date')
        end_date = self.form.cleaned_data.get('end_date')

        if not start_date or not end_date:
            raise ValidationError(_("Both 'start_date' and 'end_date' parameters are required"))

        if start_date > end_date:
            raise ValidationError(_('Start date can not be ahead of End date'))

        return super().qs


class UserFilter(UserFilter):
    """
    Example request: /?role=Mechanic&status=Archived&ordering=-last_name
    """
    ordering = filters.OrderingFilter(
        fields=(
            ('email', 'email'),
            ('first_name', 'first_name'),
            ('last_name', 'last_name'),
            ('groups__name', 'role'),
        )
    )

    class Meta:
        model = User
        fields = ('role', 'status',)


class ReportsByUsersHoursFilter(DateRangeFilterMixin, filters.FilterSet):
    """
    Example request: /?start_date=09/13/2019&end_date=10/13/2020
    """
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte', distinct=True)
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte', distinct=True)

    class Meta:
        model = IndirectHours
        fields = ('start_date', 'end_date',)


class ServiceTicketFullFilter(DateRangeFilterMixin, filters.FilterSet):
    """
    Example request: /?start_date=09/13/19&end_date=10/13/19&ordering=-number
    """
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte')
    status = filters.NumberFilter(field_name='status', lookup_expr='exact')
    search = filters.CharFilter(method='search_filter', label='Search')

    def search_filter(self, qs, name, value):
        qs = qs.select_related('created_by').prefetch_related('employee_works').\
            filter(Q(created_by__first_name__icontains=value) | Q(created_by__last_name__icontains=value) |
                   Q(connected_job__number__icontains=value) |
                   Q(employee_works__employee__first_name__icontains=value) |
                   Q(employee_works__employee__last_name__icontains=value)
                   ).distinct()
        return qs

    ordering = filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('status', 'status'),
            ('creation_date', 'date'),
            ('connected_job__number', 'number'),
            ('created_by__first_name', 'created_by'),
            ('requester__first_name', 'requested_by'),
            ('approval__first_name', 'approved_by'),
            ('connected_job__location__name', 'location'),
            ('connected_job__customer__name', 'customer'),
            ('submitted_for_approval_timestamp', 'submitted_for_approval_timestamp'),
            ('approved_timestamp', 'approved_timestamp'),
        )
    )

    class Meta:
        model = ServiceTicket
        fields = ('start_date', 'end_date', 'status', 'search')
