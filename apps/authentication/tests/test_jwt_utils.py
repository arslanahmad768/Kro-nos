from django.test import TestCase

from rest_framework.exceptions import ValidationError

from apps.api.constants import US_STATES
from ..jwt_utils import create_token, response_with_token, jwt_response_payload_handler
from ..serializers import UserSerializer
from .factories import SuperuserFactory


class MockRequest:

    def __init__(self):
        self.META = {'HTTP_USER_AGENT': ""}


class TestJWTUtils(TestCase):

    def setUp(self):
        self.user = SuperuserFactory()
        self.user_data = {
            "first_name": "Abraham",
            "last_name": "Yoba",
            "email": "webpack@pack.ck",
            "phone": "+380698569986",
        }

    def test_response_with_token(self):
        response = response_with_token(self.user, self.user_data)
        self.assertTrue('token' and 'user' in response)
        self.assertDictEqual(self.user_data, response.get('user'))

    def test_jwt_response_payload_handler(self):
        token = create_token(self.user)
        request = MockRequest()
        self.user.is_confirmed_email = True
        self.user.save()
        serialized_user = UserSerializer(self.user).data
        response = jwt_response_payload_handler(token, user=self.user, request=request)
        self.assertTrue('token' and 'user' and 'user_roles' in response)
        self.assertEqual(
            len(response.get('user').get('permissions')), len(self.user.get_all_permissions())
        )
        self.assertEqual(len(response.get('states')), len(US_STATES))
