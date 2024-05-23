from django_filters import rest_framework as filters

from .models import User
from apps.utils.filters import IntegerChoiceFilter


class UserFilter(filters.FilterSet):
    """
    Example request: /?role=Mechanic&status=Archived&ordering=-role
    """
    role = filters.CharFilter(field_name='groups__name', lookup_expr='iexact')
    status = IntegerChoiceFilter(choices=User.STATUSES)
    ordering = filters.OrderingFilter(
        fields=(
            ('first_name', 'name'),
            ('groups__name', 'role'),
            ('email', 'email'),
        )
    )

    class Meta:
        model = User
        fields = ('role', 'status',)
