from django.db import migrations
from django.db.models import Q

from apps.notifications.models import Action


def change_action_is_viewed(apps, _):
    Job = apps.get_model('api', 'Job')
    ServiceTicket = apps.get_model('api', 'ServiceTicket')
    archive_job = Job.objects.filter(is_archive=True).values_list('id', flat=True)
    archive_st = ServiceTicket.objects.filter(is_archive=True).values_list('id', flat=True)
    Action.objects.filter(
        Q(connected_object_id__in=archive_job, object_type=0) |  # OBJECT_TYPES Jobh
        Q(connected_object_id__in=archive_st, object_type=1)  # OBJECT_TYPES ST
    ).update(is_viewed=True)


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20200120_1647'),
    ]

    operations = [
        migrations.RunPython(change_action_is_viewed),
    ]
