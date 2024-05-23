from rest_framework import serializers

from apps.authentication.models import User, Mechanic
from apps.authentication.serializers import UserSerializer
from apps.api.models import ServiceTicket
from apps.api.serializers import EmployeeWorkBlockSerializer, CustomerSerializer
from apps.time_tracker.models import IndirectHours, TimeCode
from apps.utils.communication import truncate
from apps.utils.fields import IntegerChoiceField
from apps.api.constants import US_STATES


class ReportsByUsersSerializer(UserSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'role',
        )


class ReportsByServiceTicketsSerializer(serializers.ModelSerializer):

    employee_works = EmployeeWorkBlockSerializer(many=True)
    state = IntegerChoiceField(choices=US_STATES)
    status = IntegerChoiceField(choices=ServiceTicket.STATUSES)
    mileage = serializers.SerializerMethodField()
    employee = serializers.SerializerMethodField()
    hotel = serializers.SerializerMethodField()
    per_diem = serializers.SerializerMethodField()

    class Meta:
        model = ServiceTicket
        fields = (
            'id', 'status', 'requester', 'approval', 'connected_job', 'employee_works', 'created_by',
            'date', 'unit', 'lease_name', 'county', 'state',
            'customer_po_wo', 'who_called', 'engine_model', 'engine_serial',
            'comp_model', 'comp_serial', 'unit_hours', 'rpm', 'suction', 'discharge1',
            'discharge2', 'discharge3', 'safety_setting_lo1', 'safety_setting_lo2',
            'safety_setting_lo3', 'safety_setting_lo4', 'safety_setting_lo5', 'safety_setting_hi1',
            'safety_setting_hi2', 'safety_setting_hi3', 'safety_setting_hi4', 'safety_setting_hi5',
            'engine_oil_pressure', 'engine_oil_temp', 'compressor_oil_pressure',
            'compressor_oil_temp', 'ts1', 'ts2', 'ts3', 'ts4', 'td1', 'td2', 'td3', 'td4',
            'cylinder_temperature_hi1', 'cylinder_temperature_hi2', 'cylinder_temperature_hi3',
            'cylinder_temperature_hi4', 'exhaust_temperature_l', 'exhaust_temperature_r',
            'exhaust_temperature_hi', 'manifold_temperature_l', 'manifold_temperature_r',
            'manifold_temperature_hi', 'manifold_pressure_l', 'manifold_pressure_r',
            'manifold_pressure_hi1', 'manifold_pressure_hi2', 'lo_hi', 'jacket_water_pressure',
            'mmcfd', 'aux_temp', 'hour_meter_reading', 'what_was_the_call', 'what_was_found',
            'what_was_performed', 'future_work_needed', 'additional_notes',
            'customer_signature', 'customer_printed_name', 'reject_description',
            'submitted_for_approval_timestamp', 'approved_timestamp', 'mileage',
            'employee', 'hotel', 'per_diem',

        )
        read_only_fields = fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['created_by'] = {
            'first_name': instance.created_by.first_name,
            'last_name': instance.created_by.last_name,
        }

        if instance.requester:
            representation['requester'] = {
                'first_name': instance.requester.first_name,
                'last_name': instance.requester.last_name,
            }

        if instance.approval:
            representation['approval'] = {
                'first_name': instance.approval.first_name,
                'last_name': instance.approval.last_name,
            }

        representation['connected_job'] = {
            'id': instance.connected_job.id,
            'status': instance.connected_job.status,
            'number': instance.connected_job.number,
            'customer': CustomerSerializer(instance=instance.connected_job.customer).data,
            'location': instance.connected_job.location.name
        }

        return representation

    def get_mileage(self, st_instance):
        return st_instance.total_mileage

    def get_employee(self, st_instance):
        return st_instance.list_all_employees

    def get_hotel(self, st_instance):
        return st_instance.sum_hotel_checkboxes

    def get_per_diem(self, st_instance):
        return st_instance.sum_per_diem_checkboxes


class ServiceTicketsDetailedHoursSerializer(serializers.Serializer):

    status = IntegerChoiceField(choices=ServiceTicket.STATUSES)
    hours = serializers.SerializerMethodField()

    class Meta:
        fields = ('status', 'hours',)

    def __init__(self, filtered_mechanic_qs=None, **kwargs):
        """
        filtered_mechanic_qs - mechanic service tickets filtered by date range and status queryset
        """
        self.filtered_mechanic_qs = filtered_mechanic_qs
        super().__init__(**kwargs)

    def get_hours(self, obj):
        hours = 0
        for item in self.filtered_mechanic_qs:
            hours += self.calculate_elapsed_time_in_hours(item, self.context.get('employee_id'))
        return truncate(hours, 2)

    @staticmethod
    def calculate_elapsed_time_in_hours(obj, employee_id):
        difference_in_hours = 0
        for item in obj.employee_works.filter(service_ticket__pk=obj.pk, employee__id=employee_id):
            if item.hours_worked is not None:
                difference_in_hours += item.hours_worked.total_seconds() / 3600
        return truncate(difference_in_hours, 2)


class ServiceTicketsHoursSerializer(serializers.ModelSerializer):

    sum = serializers.SerializerMethodField()
    hours = serializers.SerializerMethodField()

    class Meta:
        model = ServiceTicket
        fields = ('sum', 'hours',)

    def get_sum(self, queryset):
        """
        queryset - mechanic's service tickets filtered by date range queryset
        """
        sum_of_hours = 0
        for item in queryset.all():
            sum_of_hours += ServiceTicketsDetailedHoursSerializer.calculate_elapsed_time_in_hours(
                item, self.context.get('employee_id')
            )
        return truncate(sum_of_hours, 2)

    def get_hours(self, mechanic_service_tickets_qs):
        open_data = self._serialize_data_by_status(
            mechanic_service_tickets_qs, status_type=ServiceTicket.OPEN 
        )
        pending_data = self._serialize_data_by_status(
            mechanic_service_tickets_qs, status_type=ServiceTicket.PENDING_FOR_APPROVAL
        )
        rejected_data = self._serialize_data_by_status(
            mechanic_service_tickets_qs, status_type=ServiceTicket.REJECTED
        )
        approved_data = self._serialize_data_by_status(
            mechanic_service_tickets_qs, status_type=ServiceTicket.APPROVED
        )
        return open_data, pending_data, rejected_data, approved_data

    def _serialize_data_by_status(self, qs, status_type):
        filtered_queryset = qs.filter(status=status_type)
        serializer = ServiceTicketsDetailedHoursSerializer(
            data={'status': status_type},
            filtered_mechanic_qs=filtered_queryset,
            context={'employee_id': self.context.get('employee_id')}
        )
        serializer.is_valid(raise_exception=True)
        return serializer.data


class IndirectHoursByStatusesSerializer(serializers.Serializer):

    status = IntegerChoiceField(choices=IndirectHours.STATUSES)
    hours = serializers.SerializerMethodField()

    class Meta:
        fields = ('status', 'hours',)

    def __init__(self, filtered_mechanic_qs=None, **kwargs):
        self.filtered_mechanic_qs = filtered_mechanic_qs
        super().__init__(**kwargs)

    def get_hours(self, qs):
        elapsed_time = 0
        for item in self.filtered_mechanic_qs.all():
            elapsed_time += item.hours
        return truncate(elapsed_time, 2)


class IndirectDetailedHoursByTimeCodeSerializer(serializers.ModelSerializer):

    time_code = serializers.CharField(source='name')
    sum = serializers.SerializerMethodField()
    hours = serializers.SerializerMethodField()

    class Meta:
        model = TimeCode
        fields = ('time_code', 'sum', 'hours',)

    def __init__(self, instance=None, mechanic_indirect_hours_qs=None, **kwargs):
        self.mechanic_indirect_hours_qs = mechanic_indirect_hours_qs
        super().__init__(instance, **kwargs)

    def get_sum(self, obj):
        sum_of_hours = 0
        for item in self.mechanic_indirect_hours_qs.filter(time_code__name=obj.name):
            sum_of_hours += item.hours
        return truncate(sum_of_hours, 2)

    def get_hours(self, obj):
        pending_data = self._serialize_data_by_status(obj, IndirectHours.PENDING_FOR_APPROVAL)
        rejected_data = self._serialize_data_by_status(obj, IndirectHours.REJECTED)
        approved_data = self._serialize_data_by_status(obj, IndirectHours.APPROVED)
        return pending_data, rejected_data, approved_data

    def _serialize_data_by_status(self, obj, status_type):
        filtered_queryset = self.mechanic_indirect_hours_qs.filter(
            time_code__name=obj.name, status=status_type
        )
        serializer = IndirectHoursByStatusesSerializer(
            data={'status': status_type}, filtered_mechanic_qs=filtered_queryset
        )
        serializer.is_valid(raise_exception=True)
        return serializer.data


class IndirectHoursSerializer(serializers.ModelSerializer):

    sum = serializers.SerializerMethodField()
    hours = serializers.SerializerMethodField()

    class Meta:
        model = IndirectHours
        fields = ('sum', 'hours')

    def get_sum(self, mechanic_indirect_hours_qs):
        sum_of_hours = 0
        for item in mechanic_indirect_hours_qs.all():
            sum_of_hours += item.hours
        return truncate(sum_of_hours, 2)

    def get_hours(self, mechanic_indirect_hours_qs):
        return IndirectDetailedHoursByTimeCodeSerializer(
            TimeCode.objects.all(),
            mechanic_indirect_hours_qs=mechanic_indirect_hours_qs,
            many=True
        ).data


class IndirectHoursReportSerializer(serializers.ModelSerializer):

    mechanic = serializers.StringRelatedField(many=True)
    time_code = serializers.StringRelatedField()

    class Meta:
        model = IndirectHours
        fields = ('mechanic', 'date', 'hours', 'time_code', 'notes')


class DetailedReportByMechanicSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source="get_full_name")
    sum = serializers.SerializerMethodField()
    service_tickets_hours = serializers.SerializerMethodField()
    indirect_hours = serializers.SerializerMethodField()

    class Meta:
        model = Mechanic
        fields = ('full_name', 'sum', 'service_tickets_hours', 'indirect_hours',)

    def __init__(self, instance=None,
                 mechanic_service_tickets_hours_qs=None,
                 mechanic_indirect_hours_qs=None,
                 **kwargs):
        self.mechanic_service_tickets_hours_qs = mechanic_service_tickets_hours_qs
        self.mechanic_indirect_hours_qs = mechanic_indirect_hours_qs
        super().__init__(instance, **kwargs)

    def get_sum(self, obj):
        service_tickets_hours = self.get_service_tickets_hours(obj)['sum']
        mechanic_indirect_hours = self.get_indirect_hours(obj)['sum']
        return truncate(float(service_tickets_hours) + float(mechanic_indirect_hours), 2)

    def get_service_tickets_hours(self, obj):
        return ServiceTicketsHoursSerializer(
            self.mechanic_service_tickets_hours_qs, context={'employee_id': obj.id}
        ).data

    def get_indirect_hours(self, obj):
        return IndirectHoursSerializer(self.mechanic_indirect_hours_qs).data
