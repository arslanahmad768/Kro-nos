from django.test import TestCase

from apps.authentication.tests.factories import MechanicFactory
from .factories import ActionFactory
from ..serializers import ActionSerializer


class TestActionSerializer(TestCase):

    def setUp(self):
        self.mechanic = MechanicFactory()
        self.action = ActionFactory(connected_users=(self.mechanic,))

    def test_get_valid_user_fields(self):
        serializer = ActionSerializer(self.action)
        self.assertEqual(serializer.data.get('id'), self.action.id)
        self.assertEqual(
            serializer.data.get('connected_object_id'), self.action.connected_object_id
        )
        self.assertEqual(serializer.data.get('description'), self.action.description)
        self.assertEqual(serializer.data.get('object_type').get('value'), self.action.object_type)
