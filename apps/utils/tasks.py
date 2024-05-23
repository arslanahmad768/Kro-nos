import uuid

from urllib.parse import urlencode

from django.conf import settings
from django.core.cache import cache
from django.utils.translation import gettext as _

from celery import shared_task

from .communication import encode_dict_to_base64
from .user_email_interface import UserEmail


GO_HOME_PAGE = "?goBack=/jobs"


class UserConfirmationEmail(UserEmail):

    def __init__(self, *args, **kwargs):
        super(UserConfirmationEmail, self).__init__(*args, **kwargs)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _('email confirmation')

    def cache_result(self):
        cache.set(f'email_confirmation_{self.user.id}', self.get_user_dict(), timeout=3600*12)

    def send(self):
        # relative url for client side to verify user account
        self.cache_result()
        hash_value = urlencode({'hash': encode_dict_to_base64(self.get_user_dict())})
        extra_context = {'email_confirmation_link': f'/api/v1/auth/confirm_email/?{hash_value}'}
        email = self.create_html_email(
            template='auth/email_confirmation.html',
            extra_context=extra_context
        )
        self.send_email(email)


class UserPasswordRestoreEmail(UserEmail):

    def __init__(self, *args, **kwargs):
        super(UserPasswordRestoreEmail, self).__init__(*args, **kwargs)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _('restore password')

    def cache_result(self):
        cache.set(f'password_restore_{self.user.id}', self.get_user_dict(), timeout=3600)

    def send(self):
        self.cache_result()
        # TODO generate restore link with right host
        hash_value = urlencode({'hash': encode_dict_to_base64(self.get_user_dict())})
        extra_context = {'restore_password_link': f'{settings.FRONT_HOST}/auth/restore_password/?{hash_value}'}
        email = self.create_html_email(
            template='auth/restore_password.html',
            extra_context=extra_context,
        )
        self.send_email(email)


class UserCreatedNotificationEmail(UserEmail):

    def __init__(self, *args, **kwargs):
        super(UserCreatedNotificationEmail, self).__init__(*args, **kwargs)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _('registration completed')
        self.password = kwargs.get('password')

    def send(self):
        extra_context = {'password': self.password}
        email = self.create_html_email(
            template='auth/success_registration.html',
            extra_context=extra_context,
        )
        self.send_email(email)


class UserPasswordResetEmail(UserEmail):

    def __init__(self, *args, **kwargs):
        super(UserPasswordResetEmail, self).__init__(*args, **kwargs)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _('password has been reset')
        self.password = kwargs.get('password')

    def send(self):
        extra_context = {'password': self.password}
        email = self.create_html_email(
            template='auth/reset_password.html',
            extra_context=extra_context,
        )
        self.send_email(email)


# Notifications Jobs
class UserAssignedToJob(UserEmail):

    def __init__(self, obj_id, subject, *args, **kwargs):
        super(UserAssignedToJob, self).__init__(*args, **kwargs)
        from apps.api.models import Job
        self.job = Job.objects.get(id=obj_id)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _(subject)

    def send(self):
        extra_context = {
            'link_job': f'{settings.FRONT_HOST}/jobs/edit/{self.job.id}{GO_HOME_PAGE}',
            'job_number': self.job.number
        }
        email = self.create_html_email(
            template='jobs/assign.html',
            extra_context=extra_context
        )
        self.send_email(email)


class RequestJobClosing(UserEmail):

    def __init__(self, obj_id, subject, *args, **kwargs):
        super(RequestJobClosing, self).__init__(*args, **kwargs)
        from apps.api.models import Job
        self.job = Job.objects.get(id=obj_id)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _(subject)

    def send(self):
        extra_context = {
            'link_job': f'{settings.FRONT_HOST}/jobs/edit/{self.job.id}{GO_HOME_PAGE}',
            'job_number': self.job.number
        }
        email = self.create_html_email(
            template='jobs/request_to_close.html',
            extra_context=extra_context
        )
        self.send_email(email)


class RequestJobRejected(UserEmail):

    def __init__(self, obj_id, subject, *args, **kwargs):
        super(RequestJobRejected, self).__init__(*args, **kwargs)
        from apps.api.models import Job
        self.job = Job.objects.get(id=obj_id)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _(subject)

    def send(self):
        extra_context = {
            'link_job': f'{settings.FRONT_HOST}/jobs/edit/{self.job.id}{GO_HOME_PAGE}',
            'job_number': self.job.number
        }
        email = self.create_html_email(
            template='jobs/reject.html',
            extra_context=extra_context
        )
        self.send_email(email)


# Notifications ST
class RequestStClosing(UserEmail):

    def __init__(self, obj_id, subject, *args, **kwargs):
        super(RequestStClosing, self).__init__(*args, **kwargs)
        from apps.api.models import ServiceTicket
        self.st = ServiceTicket.objects.get(id=obj_id)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _(subject)

    def send(self):
        extra_context = {
            'link_job': f'{settings.FRONT_HOST}/service_tickets/edit/{self.st.id}{GO_HOME_PAGE}',
            'st_id': self.st.id,
            'job_number': self.st.connected_job.number
        }
        email = self.create_html_email(
            template='service_tickets/sent_for_approve.html',
            extra_context=extra_context
        )
        self.send_email(email)


class RequestStRejected(UserEmail):

    def __init__(self, obj_id, subject, *args, **kwargs):
        super(RequestStRejected, self).__init__(*args, **kwargs)
        from apps.api.models import ServiceTicket
        self.st = ServiceTicket.objects.get(id=obj_id)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _(subject)

    def send(self):
        extra_context = {
            'link_job': f'{settings.FRONT_HOST}/service_tickets/edit/{self.st.id}{GO_HOME_PAGE}',
            'st_id': self.st.id,
            'job_number': self.st.connected_job.number
        }
        email = self.create_html_email(
            template='service_tickets/reject.html',
            extra_context=extra_context
        )
        self.send_email(email)


class RequestStApproved(UserEmail):

    def __init__(self, obj_id, subject, *args, **kwargs):
        super(RequestStApproved, self).__init__(*args, **kwargs)
        from apps.api.models import ServiceTicket
        self.st = ServiceTicket.objects.get(id=obj_id)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _(subject)

    def send(self):
        extra_context = {
            'link_job': f'{settings.FRONT_HOST}/service_tickets/edit/{self.st.id}{GO_HOME_PAGE}',
            'st_id': self.st.id,
            'job_number': self.st.connected_job.number
        }
        email = self.create_html_email(
            template='service_tickets/approve.html',
            extra_context=extra_context
        )
        self.send_email(email)


# Notifications Indirect hours
class SubmittedIndirectHours(UserEmail):

    def __init__(self, obj_id, subject, mechanic_name, *args, **kwargs):
        super(SubmittedIndirectHours, self).__init__(*args, **kwargs)
        from apps.time_tracker.models import IndirectHours
        self.ih = IndirectHours.objects.get(id=obj_id)
        self.mechanic = mechanic_name
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _(subject)

    def send(self):
        extra_context = {
            'link_job': f'{settings.FRONT_HOST}/indirect_hours/edit/{self.ih.id}{GO_HOME_PAGE}',
            'mechanic': self.mechanic,
            'hours': self.ih.hours
        }
        email = self.create_html_email(
            template='reports/indirect_hours.html',
            extra_context=extra_context
        )
        self.send_email(email)


# Celery tasks
def _send_email(user_id, email_class, password=None):
    if not issubclass(email_class, UserEmail):
        raise TypeError('"email_class" argument must be a subclass of UserEmail')
    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = User.objects.get(id=user_id)
    user_email = email_class(user=user, uuid=uuid.uuid4(), password=password)
    user_email.send()

def get_value_for_key(dictionaries, key_to_compare):
    """
    Retrieves the value corresponding to the given key from a list of dictionaries.
    
    """
    for dictionary in dictionaries:
        if key_to_compare in dictionary:
            return dictionary[key_to_compare]
    return None


# Celery tasks notifications
def _send_email_notifications(action_id, email_class, obj_id, mechanic_names=""):
    if not issubclass(email_class, UserEmail):
        raise TypeError('"email_class" argument must be a subclass of UserEmail')
    from apps.notifications.models import Action
    action = Action.objects.get(id=action_id)
    users = action.connected_users.filter(sent_email_notifications=True)
    print("users is------",users)
    mechanic_name = get_value_for_key(mechanic_names, action_id)
    subject = action.description
    for user in users:
        user_email = email_class(user=user, uuid=uuid.uuid4(), obj_id=obj_id, subject=subject, mechanic_name = mechanic_name)
        user_email.send()


@shared_task
def send_email_confirmation_link(user_id):
    _send_email(user_id, UserConfirmationEmail)


@shared_task
def send_password_restore_link(user_id):
    _send_email(user_id, UserPasswordRestoreEmail)


@shared_task
def send_notification_user_created(user_id, password):
    _send_email(user_id, UserCreatedNotificationEmail, password)


@shared_task
def send_reset_password(user_id, password):
    _send_email(user_id, UserPasswordResetEmail, password)


def _send_pusher_beams_notification(action_id, message):
    from apps.notifications.models import Action
    action = Action.objects.get(id=action_id)
    from apps.notifications.notification_interface import PusherBeamsNotification
    notification = PusherBeamsNotification(action, message % str(action.connected_object_id))
    notification.send()


def _send_pusher_channels_notification(action_id):
    from apps.notifications.models import Action
    action = Action.objects.get(id=action_id)
    from apps.notifications.notification_interface import PuscherChannelsNotification
    notification = PuscherChannelsNotification(action)
    notification.send()


# Notifications
@shared_task
def send_users_has_been_assigned_to_job(obj_id, action_ids):
    for action_id in action_ids:
        _send_email_notifications(action_id, UserAssignedToJob, obj_id)
        _send_pusher_channels_notification(action_id)
        _send_pusher_beams_notification(action_id, 'You have been assigned to a Job #%s')


@shared_task
def send_request_job_closing(obj_id, action_id):
    _send_email_notifications(action_id, RequestJobClosing, obj_id)
    _send_pusher_channels_notification(action_id)


@shared_task
def send_request_job_rejected(obj_id, action_id):
    _send_email_notifications(action_id, RequestJobRejected, obj_id)
    _send_pusher_channels_notification(action_id)


@shared_task
def send_request_st_closing(obj_id, action_id):
    _send_email_notifications(action_id, RequestStClosing, obj_id)
    _send_pusher_channels_notification(action_id)


@shared_task
def send_request_st_rejected(obj_id, action_id):
    _send_email_notifications(action_id, RequestStRejected, obj_id)
    _send_pusher_channels_notification(action_id)
    _send_pusher_beams_notification(action_id, 'Service Ticket #%s has been Rejected')


@shared_task
def send_request_st_approved(obj_id, action_id):
    _send_email_notifications(action_id, RequestStApproved, obj_id)
    _send_pusher_channels_notification(action_id)
    _send_pusher_beams_notification(action_id, 'Service Ticket #%s has been Approved')


@shared_task
def send_submitted_ih(obj_id, action_id,mechanic_names):
    for actionID in action_id:
        _send_email_notifications(actionID, SubmittedIndirectHours, obj_id,mechanic_names)
        _send_pusher_channels_notification(actionID)
