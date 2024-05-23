from decimal import Decimal

from django.test import TestCase
from unittest.mock import patch

from apps.authentication.tests.factories import MechanicFactory, ManagerFactory, AdminFactory
from .factories import IndirectHoursFactory, TimeCodeFactory
from ..models import IndirectHours
from ..serializers import IndirectHoursReadSerializer, IndirectHoursWriteSerializer
from ...api.tests.test_model_validators import MockedRequest


class TestIndirectHoursSerializer(TestCase):

    def setUp(self):
        self.indirect = IndirectHoursFactory()

    def test_get_valid_user_fields(self):
        serializer = IndirectHoursReadSerializer(self.indirect)
        self.assertEqual(serializer.data.get('id'), self.indirect.id)
        self.assertEqual(serializer.data.get('date'), self.indirect.date.strftime('%m-%d-%Y'))
        self.assertEqual(Decimal(serializer.data.get('hours')), Decimal(self.indirect.hours))
        self.assertEqual(serializer.data.get('time_code').get('id'), self.indirect.time_code.id)
        self.assertEqual(serializer.data.get('notes'), self.indirect.notes)
        self.assertEqual(serializer.data.get('mechanic').get('id'), self.indirect.mechanic.id)

    def test_validate_create_wrong_status(self):
        mechanic = MechanicFactory()
        time_code = TimeCodeFactory()
        data = {
            'status': 2,
            'date': '12-27-2020',
            'hours': 5,
            'time_code': time_code.id,
            'notes': 'notes',
            'mechanic': mechanic.id
        }
        serializer = IndirectHoursReadSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    @patch('apps.api.models.RequestMiddleware')
    def test_validate_pending_status_admin(self, mocked_req):
        mocked_req.get_request.return_value = MockedRequest(user=AdminFactory())
        new_ih = IndirectHoursFactory(status=IndirectHours.PENDING_FOR_APPROVAL)
        new_ih.notes = 'wrong field changed'
        serializer = IndirectHoursWriteSerializer(data=new_ih)
        self.assertFalse(serializer.is_valid())

    @patch('apps.api.models.RequestMiddleware')
    def test_validate_pending_status_manager(self, mocked_req):
        mocked_req.get_request.return_value = MockedRequest(user=ManagerFactory())
        new_ih = IndirectHoursFactory(status=IndirectHours.PENDING_FOR_APPROVAL)
        new_ih.notes = 'wrong field changed'
        serializer = IndirectHoursWriteSerializer(data=new_ih)
        self.assertFalse(serializer.is_valid())

    @patch('apps.api.models.RequestMiddleware')
    def test_validate_approved_status_admin(self, mocked_req):
        mocked_req.get_request.return_value = MockedRequest(user=AdminFactory())
        new_ih = IndirectHoursFactory(status=IndirectHours.APPROVED)
        new_ih.notes = 'wrong field changed'
        serializer = IndirectHoursWriteSerializer(data=new_ih)
        self.assertFalse(serializer.is_valid())
