from django.utils.translation import gettext_lazy as _

from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError


class IntegerChoiceFilter(filters.Filter):
    """
    It can be reused in all filtersets when you need filtering by two-tuples second argument.
    Common example is model IntegerFiled with choices.
    """
    def __init__(self, choices, **kwargs):
        super().__init__(distinct=True, **kwargs)
        self.choices = {status.lower(): id for (id, status) in choices}

    def filter(self, qs, value):
        id = self.choices.get(value.lower() if value is not None else value, None)
        # raise an error if id does not exist in choices and filtering value is not None
        if id is None and value is not None:
            raise ValidationError({
                self.field_name: [_(f'Select a valid choice. {value} is not one of the '
                                    'available choices.')]
            })

        return super().filter(qs, id)
