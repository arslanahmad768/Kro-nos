from django.db import transaction

from apps.authentication.models import Manager, Admin, Biller
from apps.notifications.models import Action
from apps.utils.tasks import (
    send_request_job_closing, send_request_job_rejected,
    send_request_st_closing, send_request_st_rejected,
    send_request_st_approved, send_submitted_ih
)


class ActionNotifications(object):

    def _create_action(self, object_type, description):
        action = Action.objects.create(
            object_type=object_type,
            connected_object_id=self.id,
            description=description
        )
        return action

    def _check_status(self, status):
        if self.status == status and not self._original_status == status:
            return True
        return False


class JobActionNotifications(ActionNotifications):

    def _request_job_closing(self):
        if self._check_status(self.PENDING_FOR_APPROVAL):
            action = self._create_action(
                Action.JOB,
                f'You have been requested to Close the Job - "{self.number}"'
            )
            if self.requester.is_manager:
                for biller in Biller.objects.all():
                    action.connected_users.add(biller)
                transaction.on_commit(lambda: send_request_job_closing.delay(
                    self.id, action.id
                ))
            elif self.requester.is_biller:
                for manager in self.managers.all():
                    action.connected_users.add(manager)
                transaction.on_commit(lambda: send_request_job_closing.delay(
                    self.id, action.id
                ))

    def _job_has_been_rejected(self):
        if self._check_status(self.REJECTED):
            action = self._create_action(
                Action.JOB,
                f'The Job - "{self.number}" has been Rejected'
            )
            for manager in self.managers.all():
                action.connected_users.add(manager)
            transaction.on_commit(lambda: send_request_job_rejected.delay(
                self.id, action.id
            ))

    @property
    def run_notifications(self):
        self._request_job_closing()
        self._job_has_been_rejected()


class ServiceTicketActionNotifications(ActionNotifications):

    def _check_if_there_is_a_requester(self):
        if self.requester is None:
            return False
        return True

    def _request_st_approval(self):
            if self._check_status(self.PENDING_FOR_APPROVAL):
                action = self._create_action(
                    Action.ST,
                    f'The Service Ticket - "{self.id}" for the Job - "{self.connected_job.number}" has been Submitted for Approval'
                )
                for manager in self.connected_job.managers.all():
                    action.connected_users.add(manager)  
                action.connected_users.add(self.requester_id)
                transaction.on_commit(lambda: send_request_st_closing.delay(
                    self.id, action.id
                ))
                
    def _st_has_been_rejected(self):
        if self._check_status(self.REJECTED) and self._check_if_there_is_a_requester():
            action = self._create_action(
                Action.ST,
                f'The Service Ticket - "{self.id}" for the Job - "{self.connected_job.number}" has been Rejected'
            )
            action.connected_users.add(self.requester)
            transaction.on_commit(lambda: send_request_st_rejected.delay(
                self.id, action.id
            ))

    def _st_has_been_approved(self):
        if self._check_status(self.APPROVED) and self._check_if_there_is_a_requester():
            action = self._create_action(
                Action.ST,
                f'The Service Ticket - "{self.id}" for the Job - "{self.connected_job.number}" has been Approved'
            )
            action.connected_users.add(self.requester)
            transaction.on_commit(lambda: send_request_st_approved.delay(
                self.id, action.id
            ))

    @property
    def run_notifications(self):
        self._request_st_approval()
        self._st_has_been_rejected()
        self._st_has_been_approved()


class IndirectHoursActionNotifications(ActionNotifications):

    def _ih_has_been_submitted(self):
        if self.status == self.PENDING_FOR_APPROVAL:
            action = self._create_action(
                Action.INDIRECT_HOUR,
                f'"{self.hours}" Indirect Hours have been Submitted for - "{str(self.mechanic)}"'
            )

            for manager in Manager.objects.filter(id=self.mechanic.manager.id):
                action.connected_users.add(manager)
        transaction.on_commit(lambda: send_submitted_ih.delay(self.id, action.id))

    @property
    def run_notifications(self):
        self._ih_has_been_submitted()
