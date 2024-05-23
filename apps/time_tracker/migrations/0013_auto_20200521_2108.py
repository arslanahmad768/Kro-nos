from django.db import migrations

from apps.notifications.models import Action


def change_action_is_viewed(apps, _):
    IndirectHours = apps.get_model('time_tracker', 'IndirectHours')
    ih = IndirectHours.objects.filter(is_archive=True).values_list('id', flat=True)
    Action.objects.filter(
        connected_object_id__in=ih,
        object_type=2  # OBJECT_TYPES INDIRECT_HOUR
    ).update(is_viewed=True)


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0012_auto_20200313_1531'),
    ]

    operations = [
        migrations.RunPython(change_action_is_viewed),
    ]
