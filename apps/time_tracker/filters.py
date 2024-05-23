import rest_framework_filters as filters

from apps.utils.filters import IntegerChoiceFilter
from .models import IndirectHours


class IndirectHoursFilter(filters.FilterSet):
    """
    Example request: /?status=APPROVED&start_date=01/01/20&end_date=01/03/20&ordering=-date
    """
    # TODO: update rest_framework_filters version in requirements after release
    status = IntegerChoiceFilter(choices=IndirectHours.STATUSES)
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte')
    is_archive = filters.BooleanFilter(method='filter_all_archive')
    ordering = filters.OrderingFilter(
        fields=(
            ('date', 'date'),
            ('mechanic__first_name', 'mechanic'),
            ('hours', 'hours'),
            ('time_code', 'time_code'),
            ('status', 'status'),
            ('notes', 'notes'),
        )
    )

    def filter_all_archive(self, queryset, name, value):
        if value != True:
            return queryset
        queryset = IndirectHours.objects.filter(is_archive=True).order_by('-creation_date')
        return queryset

    class Meta:
        model = IndirectHours
        fields = ('status', 'start_date', 'end_date',)
