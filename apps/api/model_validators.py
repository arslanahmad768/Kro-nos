import os

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.utils.request_middleware import RequestMiddleware


def validate_request_job_perm(value):
    from .models import CommonInfo
    user = RequestMiddleware.get_request().user
    has_access = user.has_perm('authentication.can_set_pending_for_approval')
    if value == CommonInfo.PENDING_FOR_APPROVAL and not has_access:
        raise ValidationError(
            _('You do not have permissions to set Pending for Approval status. '
              'Contact the job Biller or Manager')
        )

def validate_attachment_file_type(file):
    file_type = os.path.splitext(file.name)[1].lower()
    if file_type not in (
        '.pdf', '.xls', '.xlsx', '.doc', '.docx', '.jpeg', '.jpg', '.png', '.gif','.heic'
    ):
        raise ValidationError(_(f'{file_type} is not supported file extension.'))
