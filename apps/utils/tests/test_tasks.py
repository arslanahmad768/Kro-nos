from django.conf import settings
from django.core import mail
from django.test import TestCase

from apps.time_tracker.tests.factories import IndirectHoursFactory
from apps.api.tests.factories import JobFactory, ServiceTicketFactory
from apps.api.utils import delete_file
from apps.authentication.tests.factories import UserFactory
from apps.notifications.tests.factories import ActionFactory
from ..tasks import (
    send_notification_user_created,
    send_reset_password, send_users_has_been_assigned_to_job,
    send_request_job_closing, send_request_job_rejected,
    send_request_st_closing, send_request_st_rejected,
    send_request_st_approved, send_submitted_ih
)


class TestSendEmailWithAttachment(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.job = JobFactory()
        self.st = ServiceTicketFactory()
        self.ih = IndirectHoursFactory()

    def tearDown(self):
        delete_file(self.st.customer_signature.path)
        for attachment in self.st.attachments.all():
            delete_file(attachment.file.path)

    def test_send_notification_user_created(self):
        send_notification_user_created(self.user.id, 'password')
        sent_email = mail.outbox[0]
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(sent_email.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_email.to[0], self.user.email)

    def test_send_reset_password(self):
        send_reset_password(self.user.id, 'password')
        sent_email = mail.outbox[0]
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(sent_email.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_email.to[0], self.user.email)

    def test_send_users_has_been_assigned_to_job(self):
        action = ActionFactory(connected_object_id=self.job.id, connected_users=(self.user,))
        send_users_has_been_assigned_to_job(self.job.id, [action.id])
        sent_email = mail.outbox[0]
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(sent_email.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_email.to[0], self.user.email)

    def test_send_request_job_closing(self):
        action = ActionFactory(connected_object_id=self.job.id, connected_users=(self.user,))
        send_request_job_closing(self.job.id, action.id)
        sent_email = mail.outbox[0]
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(sent_email.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_email.to[0], self.user.email)

    def test_send_request_job_rejected(self):
        action = ActionFactory(connected_object_id=self.job.id, connected_users=(self.user,))
        send_request_job_rejected(self.job.id, action.id)
        sent_email = mail.outbox[0]
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(sent_email.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_email.to[0], self.user.email)

    def test_send_request_st_closing(self):
        action = ActionFactory(connected_object_id=self.job.id, connected_users=(self.user,))
        send_request_st_closing(self.st.id, action.id)
        sent_email = mail.outbox[0]
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(sent_email.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_email.to[0], self.user.email)

    def test_send_request_st_rejected(self):
        action = ActionFactory(connected_object_id=self.st.id, connected_users=(self.user,))
        send_request_st_rejected(self.st.id, action.id)
        sent_email = mail.outbox[0]
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(sent_email.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_email.to[0], self.user.email)

    def test_send_request_st_approved(self):
        action = ActionFactory(connected_object_id=self.st.id, connected_users=(self.user,))
        send_request_st_approved(self.st.id, action.id)
        sent_email = mail.outbox[0]
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(sent_email.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_email.to[0], self.user.email)

    def test_send_submitted_ih(self):
        action = ActionFactory(connected_object_id=self.ih.id, connected_users=(self.user,))
        send_submitted_ih(self.ih.id, action.id)
        sent_email = mail.outbox[0]
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(sent_email.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_email.to[0], self.user.email)
