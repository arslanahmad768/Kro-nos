import uuid

from django.core import mail
from django.test import TestCase

from apps.authentication.tests.factories import UserFactory
from ..context_processors import _https_check
from ..user_email_interface import UserEmail


class TestUserEmailInterface(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user_email = UserEmail(self.user, uuid.uuid4())

    def test_get_user_dict(self):
        user_dict = self.user_email.get_user_dict()
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['uuid'], str(self.user_email.user_uuid))

    def test_https_check_with_http(self):
        value = 'http://'
        self.assertEqual(_https_check(value), value)

    def test_https_check_with_https(self):
        value = 'https://'
        self.assertEqual(_https_check(value), value)

    def test_create_email(self):
        email = self.user_email._create_email('mock_template.html')
        self.assertEqual(email.subject, self.user_email.subject)
        self.assertEqual(email.from_email, self.user_email.from_email)
        self.assertEqual(email.to, [self.user.email])
        self.assertIsNotNone(email.body)

    def test_user_sent_email_notifications_is_False(self):
        self.user.sent_email_notifications = False
        self.user.save()
        email = UserEmail(self.user, uuid.uuid4())
        email.send_email(email._create_email('mock_template.html'))
        self.assertEqual(len(mail.outbox), 0)
