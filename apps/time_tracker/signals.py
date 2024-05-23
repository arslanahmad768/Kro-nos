from django.db import transaction
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.utils.tasks import send_submitted_ih
from apps.authentication.models import Manager, Mechanic
from apps.notifications.models import Action
from apps.time_tracker.models import IndirectHours


@receiver(m2m_changed, sender=IndirectHours.mechanic.through)
def indirectHours_mechanics_changed(sender, instance, action, reverse, pk_set, *args, **kwargs):
    if action == "pre_add" and not reverse:
        mechanics = Mechanic.objects.filter(pk__in=pk_set)
        action_ids = []
        mechanic_names = []
        for mechanic in mechanics:
            managers = Manager.objects.filter(pk=mechanic.manager.id)
            for manager in managers:
                action = Action.objects.create(
                    object_type=Action.INDIRECT_HOUR,
                    connected_object_id=instance.id,
                    description=f'"{instance.hours}" Indirect Hours have been Submitted for - "{str(mechanic)}"'
                )
                action.connected_users.add(manager)
                action_ids.append(action.id)
                mechanic_names.append({action.id:mechanic.get_full_name()})
        transaction.on_commit(lambda: send_submitted_ih.delay(
            instance.id, action_ids,mechanic_names
        ))
