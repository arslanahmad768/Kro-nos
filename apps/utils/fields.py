from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db.models import DecimalField
from django.utils.functional import cached_property

from rest_framework import fields


class IntegerChoiceField(fields.ChoiceField):

    def to_representation(self, value):
        return {
            'value': value,
            'name': self.choices[value]
        }


class PositiveDecimalField(DecimalField):

        @cached_property
        def validators(self):
            return super().validators + [
                MinValueValidator(limit_value=0, message='This field must be a positive value.')
            ]


class DecimalField(PositiveDecimalField):
    """
    Custom DecimalField for this project.
    args:
        max_digits=10;
        decimal_places=1;
        null=True;
        blank=True;
    """

    def __init__(self, *args, **kwargs):
        kwargs.update({'max_digits': 10, 'decimal_places': 1, 'blank': True, 'null': True})
        super().__init__(*args, **kwargs)
