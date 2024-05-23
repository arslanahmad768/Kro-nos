from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from rest_framework.exceptions import PermissionDenied
from rest_framework_jwt.utils import jwt_encode_payload as jwt_encode_handler, jwt_create_payload as jwt_payload_handler
from rest_framework.exceptions import PermissionDenied

from apps.utils.user_agent import UserAgent
from apps.api.constants import US_STATES
from apps.utils.fields import IntegerChoiceField
from .group_permissions import USER_ROLES
from .serializers import UserSerializer
from apps.api.models import DBLockDate


def jwt_response_payload_handler(token, user=None, request=None, created_at=None):
    """Return user token and additional information for client side needs."""
    if user.is_status_archived:
        error = {
            "non_field_errors": ["This user is archived. Contact Administrator"]
        }
        raise PermissionDenied(error)
    user_roles = IntegerChoiceField(choices=USER_ROLES)
    states = IntegerChoiceField(choices=US_STATES)
    ua = UserAgent(request.META.get('HTTP_USER_AGENT', ''))
    if settings.APP_NAME.lower() in ua.ua_string.lower() and not user.is_mechanic:
        error = {
            "user_role": ["You are not a Mechanic. Contact Administrator"]
        }
        raise PermissionDenied(error)
    user_data = UserSerializer(user, context={'request': request}).data
    user_data['permissions'] = user.get_all_permissions()
    user_data['db_lock_date'] = DBLockDate.objects.get().lock_date if DBLockDate.objects.exists() else None
    data = {
        'token': token,
        'user': user_data,
        'user_roles': [
            user_roles.to_representation(value) for value in user_roles.choices
            if user_roles.choices[value] != 'Superuser'
        ],
        'states': [states.to_representation(value) for value in states.choices]
    }
    return data


def create_token(user):
    """Create token by user instanse."""
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token


def response_with_token(instance, serializer_data):
    """Create response user data with token."""
    token = create_token(instance)
    response = {
        'token': token,
        'user': serializer_data
    }
    return response
