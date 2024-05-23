from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.utils.request_middleware import RequestMiddleware


def validate_perm(value):
    from .models import IndirectHours
    user = RequestMiddleware.get_request().user
    has_rejection = user.has_perm('time_tracker.can_reject_indirect_hours')
    has_approval = user.has_perm('time_tracker.can_approve_indirect_hours')
    if value == IndirectHours.REJECTED and not has_rejection:
        raise ValidationError(
            _('You do not have permissions to set Rejected status. '
              'Contact the Manager')
        )
    if value == IndirectHours.APPROVED and not has_approval:
        raise ValidationError(
            _('You do not have permissions to set Approved status. '
              'Contact the Manager')
        )
