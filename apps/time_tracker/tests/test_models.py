from unittest.mock import patch

from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.authentication.tests.factories import UserFactory
from apps.notifications.models import Action
from .factories import IndirectHoursFactory, TimeCodeFactory
from ..models import IndirectHours, TimeCode


class MockedRequest:
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        return super().__init__(*args, **kwargs)


class TestIndirectHours(TestCase):

    def setUp(self):
        self.indirect = IndirectHoursFactory()

    def test_str_method(self):
        self.assertEqual(
            str(self.indirect),
            f'Hours of {self.indirect.mechanic}'
        )

    def test_create_ih_is_approved_status(self):
        new_ih = IndirectHoursFactory(
            status=IndirectHours.APPROVED
        ).clean()
        self.assertRaises(ValidationError, new_ih)

    def test_validate_hours_field(self):
        new_ih = IndirectHoursFactory(
            status=IndirectHours.PENDING_FOR_APPROVAL,
            hours='25'
        )
        self.assertRaises(ValidationError, new_ih.clean())

    @patch('apps.api.models.RequestMiddleware')
    def test_ih_has_been_submitted_notifications(self, mocked_req):
        mocked_req.get_request.return_value = MockedRequest(user=UserFactory())
        new_ih = IndirectHoursFactory()
        actions_before = Action.objects.filter(
            connected_object_id=new_ih.id,
        ).count()
        new_ih.status = IndirectHours.PENDING_FOR_APPROVAL
        new_ih.save()
        actions_after = Action.objects.filter(
            connected_object_id=new_ih.id,
        ).count()
        self.assertEqual(actions_after, actions_before + 1)


class TestTimeCode(TestCase):

    def setUp(self):
        self.time_code = TimeCodeFactory()

    def test_str_method(self):
        self.assertEqual(
            str(self.time_code),
            self.time_code.name
        )
