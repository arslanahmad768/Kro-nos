from django.db.models import Q

import rest_framework_filters as filters
from rest_framework import serializers

from apps.utils.filters import IntegerChoiceFilter
from .models import Job, ServiceTicket


class JobFilter(filters.FilterSet):
    """
    Example request: /?status=Open&start_date=09/13/19&end_date=10/13/19&search=WTX&all_tickets_approved=true&ordering=-number
    """
    # TODO: update rest_framework_filters version in requirements after release
    status = IntegerChoiceFilter(choices=Job.STATUSES)
    start_date = filters.DateFilter(field_name='creation_date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='creation_date', lookup_expr='lte')
    all_tickets_approved = filters.BooleanFilter(method='filter_all_tickets_approved')
    is_archive = filters.BooleanFilter(method='filter_is_archive')
    ordering = filters.OrderingFilter(
        fields=(
            ('number', 'number'),
            ('status', 'status'),
            ('created_by__first_name', 'created_by'),
            ('requester__first_name', 'requested_by'),
            ('approval__first_name', 'approved_by'),
            ('location__name', 'location'),
            ('customer__name', 'customer'),
            ('creation_date', 'time_stamp'),
        )
    )

    def filter_all_tickets_approved(self, queryset, name, value):
        if value != True:
            return queryset
        return queryset.filter(
            Q(serviceticket__status=ServiceTicket.APPROVED) | Q(serviceticket__isnull=True)
        )

    def filter_is_archive(self, queryset, name, value):
        flag = value is True
        return queryset.filter(**{'is_archive': flag})

    class Meta:
        model = Job
        fields = ('status', 'start_date', 'end_date',)


class ServiceTicketFilter(filters.FilterSet):
    """
    Example request: /?status=Open&start_date=09/13/19&end_date=10/13/19&search=WTX&ordering=-number
    """
    status = IntegerChoiceFilter(choices=ServiceTicket.STATUSES)
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte')
    is_archive = filters.BooleanFilter(method='filter_all_archive')
    job_number = filters.CharFilter(method='filter_by_job_number')
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
            ('additional_notes', 'notes'),
        )
    )

    def filter_all_archive(self, queryset, name, value):
        if value != True:
            return queryset
        queryset = ServiceTicket.objects.filter(is_archive=True).order_by('-creation_date')
        return queryset

    def filter_by_job_number(self, queryset, name, value):
        if not value:
            return queryset
        queryset = ServiceTicket.objects.filter(connected_job__number=value)
        return queryset

    class Meta:
        model = ServiceTicket
        fields = ('status', 'start_date', 'end_date',)
