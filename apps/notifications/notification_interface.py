import uuid

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from celery.utils.log import get_task_logger
from pusher import Pusher
from pusher_push_notifications import PushNotifications

from apps.utils.user_email_interface import UserEmail
from .serializers import ActionSerializer

logger = get_task_logger(__name__)


def setting_to_string(setting):
    """
    For some reason Django LazySettings make setting a tuple object instead of string.
    """
    if isinstance(setting, tuple):
        return setting[0]
    return setting


beams_client = PushNotifications(
    instance_id=setting_to_string(settings.PUSHER_INSTANCE_ID),
    secret_key=setting_to_string(settings.PUSHER_SECRET_KEY),
)

pusher_client = Pusher(
    app_id=setting_to_string(settings.PUSHER_APP_ID),
    key=setting_to_string(settings.PUSHER_KEY),
    secret=setting_to_string(settings.PUSHER_SECRET),
    cluster=setting_to_string(settings.PUSHER_CLUSTER),
    ssl=settings.PUSHER_USE_SSL
)


class ActionNotificationEmail(UserEmail):

    def __init__(self, description, *args, **kwargs):
        super(ActionNotificationEmail, self).__init__(uuid=uuid.uuid4(), *args, **kwargs)
        self.subject = settings.EMAIL_SUBJECT_PATTERN % _('email notification')
        self.description = description

    def send(self):
        extra_context = {'description': self.description}
        email = self.create_html_email(
            template='notification/email_notification.html',
            extra_context=extra_context
        )
        self.send_email(email)


class PusherBeamsNotification:
    """
    Interface to Pusher Beams notifications.
    """

    def __init__(self, action, message):
        self.action = action
        self.users = self.action.connected_users.filter(sent_push_notifications=True)
        self.message = message
        self.data = ActionSerializer(self.action).data

    def send(self):
        for user in self.users:
            if user.is_mechanic:
                beams_client.publish_to_users(
                    user_ids=[str(user.id)],
                    publish_body={
                        'apns': {
                            'aps': {
                                'alert': self.message
                            },
                            'data': {
                                'action': self.data
                            }
                        }
                    }
                )
                logger.info(f'Pusher Beams notification for {self.action} was sent to {user}.')
            else:
                logger.warning(
                    f'Pusher Beams notification for {self.action} was not sent to {user} '
                    'because only Mechanics can get Pusher notifications.'
                )


class PuscherChannelsNotification:
    """
    Interface to Pusher Channels notifications.
    """

    def __init__(self, action):
        self.action = action
        self.users = self.action.connected_users.filter(sent_push_notifications=True)
        self.event_name = 'action-created'
        self.data = ActionSerializer(self.action).data

    def send(self):
        for user in self.users:
            pusher_client.trigger(
                channels=self.generate_channels_name(user.id),
                event_name=self.event_name,
                data=self.data
            )
            logger.info(f'Pusher Channels notification for {self.action} was sent to {user}.')

    def generate_channels_name(self, user_id):
        """Currently there is can be only one channel for each user."""
        return f'channel_{user_id}'
