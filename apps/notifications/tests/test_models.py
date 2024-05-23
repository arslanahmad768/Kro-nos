from django.test import TestCase

from apps.authentication.tests.factories import MechanicFactory
from ..models import Action
from .factories import ActionFactory


class TestActionModel(TestCase):

    def setUp(self):
        self.mechanic = MechanicFactory()
        self.action = ActionFactory(connected_users=(self.mechanic,))

    def test_str_method(self):
        self.assertEqual(
            str(self.action),
            f'Action for {Action.OBJECT_TYPES[self.action.object_type][1]} #{self.action.connected_object_id}'
        )
