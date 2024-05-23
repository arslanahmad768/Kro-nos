from django.contrib.auth.models import Group
from django.test import TestCase

from apps.authentication.tests.factories import AdminFactory
from ..serializers import ReportsByUsersSerializer


class TestReportsByUsersSerializer(TestCase):

    def setUp(self):
        self.user = AdminFactory()

    def test_get_valid_user_fields(self):
        serializer = ReportsByUsersSerializer(self.user)
        self.assertEqual(serializer.data.get('id'), self.user.id)
        self.assertEqual(serializer.data.get('first_name'), self.user.first_name)
        self.assertEqual(serializer.data.get('last_name'), self.user.last_name)
        self.assertEqual(serializer.data.get('email'), self.user.email)
        self.assertEqual(
            serializer.data.get('role').get('value'),
            Group.objects.get(name=serializer.data.get('role').get('name')).id
        )
