from unittest.mock import patch

from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.authentication.tests.factories import UserFactory
from ..model_validators import validate_request_job_perm
from ..models import CommonInfo


class MockedRequest:
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        return super().__init__(*args, **kwargs)


class TestValidators(TestCase):

    @patch('apps.api.model_validators.RequestMiddleware')
    def test_validate_request_job_perm_raises_error(self, mocked_req):
        mocked_req.get_request.return_value = MockedRequest(user=UserFactory())
        error_message = 'You do not have permissions to set Pending for Approval status. '\
                        'Contact the job Biller or Manager'
        with self.assertRaisesMessage(ValidationError, error_message):
            validate_request_job_perm(CommonInfo.PENDING_FOR_APPROVAL)

    @patch('apps.api.model_validators.RequestMiddleware')
    def test_validate_request_job_perm_successfully(self, mocked_req):
        user = UserFactory(
            is_superuser=True,
            is_staff=True
        )  # superuser has access patch
        mocked_req.get_request.return_value = MockedRequest(user=user)
        self.assertIsNone(validate_request_job_perm(CommonInfo.PENDING_FOR_APPROVAL))
