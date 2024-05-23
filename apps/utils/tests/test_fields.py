from django.test import TestCase

from apps.api.models import Job
from ..fields import IntegerChoiceField


class TestIntegerChoiceField(TestCase):

    def setUp(self):
        self.choices = Job.STATUSES
        self.field = IntegerChoiceField(choices=self.choices)
        self.value = Job.OPEN

    def test_to_representation(self):
        representation = self.field.to_representation(self.value)
        self.assertEqual(representation.get('value'), self.value)
        self.assertEqual(representation.get('name'), self.field.choices[Job.OPEN])
