from datetime import datetime

from django.core.mail import EmailMessage, send_mail
from django.db import transaction
from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver

from apps.utils.tasks import send_users_has_been_assigned_to_job
from apps.authentication.models import Manager, Mechanic
from apps.notifications.models import Action
from .models import CommonInfo, Job, ServiceTicket


@receiver(m2m_changed, sender=Job.mechanics.through)
def job_mechanics_changed(sender, instance, action, reverse, pk_set, *args, **kwargs):
    if action == "pre_add" and not reverse:
        mechanics = Mechanic.objects.filter(pk__in=pk_set)
        action_ids = []
        for mechanic in mechanics:
            action = Action.objects.create(
                object_type=Action.JOB,
                connected_object_id=instance.id,
                description=f'You have been assigned to the Job - "{instance.number}"'
            )
            action.connected_users.add(mechanic)
            action_ids.append(action.id)
        transaction.on_commit(lambda: send_users_has_been_assigned_to_job.delay(
            instance.id, action_ids
        ))


@receiver(m2m_changed, sender=Job.managers.through)
def job_managers_changed(sender, instance, action, reverse, pk_set, *args, **kwargs):
    if action == "pre_add" and not reverse:
        managers = Manager.objects.filter(pk__in=pk_set)
        current_manager = instance.created_by_id
        action_ids = []
        check = False
        for manager in managers:
            if manager.id == current_manager:
                check = True
        for manager in managers:
            action = Action.objects.create(
                object_type=Action.JOB,
                connected_object_id=instance.id,
                description=f'You have been assigned to the Job - "{instance.number}"'
            )
            action.connected_users.add(manager)
            action_ids.append(action.id)
        if check is False:
            action = Action.objects.create(
                object_type=Action.JOB,
                connected_object_id=instance.id,
                description=f'Job "{instance.number}" created successfully'
            )
            action.connected_users.add(current_manager)
            action_ids.append(action.id)    
        transaction.on_commit(lambda: send_users_has_been_assigned_to_job.delay(
            instance.id, action_ids
        ))

"""
@receiver(pre_save, sender=ServiceTicket)
def service_ticket_changed(sender, instance, *args, **kwargs):
    try:
        old_status = ServiceTicket.objects.get(id=instance.id).status
        if instance.id is not None and instance.status is CommonInfo.APPROVED and old_status is not CommonInfo.APPROVED and\
                len(instance.future_work_needed) > 2:
            mechanics = ""
            for e in instance.employee_works.all():
                mechanics += "\t{}\r\n".format(e.employee.get_full_name())

            send_mail('Service Ticket # {} of Job {} approved'.format(instance.id, instance.connected_job.number),
                      'Date: {}\r\nWork Order #: {}\r\nMechanics:\r\n{}\r\nParts Used: {}'.
                      format(instance.date, instance.connected_job.number, mechanics, instance.future_work_needed),
                      'parts@kro-nos.com', ['parts@krollc.com'])
    except ServiceTicket.DoesNotExist:
        print('Just created a new Service ticket')
"""


@receiver(pre_save, sender=Job)
def job_status_changed(sender, instance, *args, **kwargs):
    try:
        old_status = Job.objects.get(id=instance.id).status

        if old_status is CommonInfo.OPEN and instance.status is CommonInfo.PENDING_FOR_APPROVAL:
            instance.request_date = datetime.now()
    except Job.DoesNotExist:
        print('created new job')
