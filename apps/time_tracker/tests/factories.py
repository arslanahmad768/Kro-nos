import factory
from factory import fuzzy

from django.utils import timezone

from apps.authentication.tests.factories import MechanicFactory

from ..models import IndirectHours, TimeCode


class TimeCodeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = TimeCode
    name = fuzzy.FuzzyText(prefix='Time_code_', length=15)


class IndirectHoursFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = IndirectHours

    status = IndirectHours.APPROVED
    date = timezone.now().date()
    hours = 5
    time_code = factory.SubFactory(TimeCodeFactory)
    notes = 'notes'
    mechanic = factory.SubFactory(MechanicFactory)
