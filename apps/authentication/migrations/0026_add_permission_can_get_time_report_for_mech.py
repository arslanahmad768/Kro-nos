from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def update_mechanic_group_perms(apps, _):
    # add a custom permission to Mechanic's group
    mechanic_group = Group.objects.get(name='Mechanic')
    Mechanic = apps.get_model('authentication', 'Mechanic')
    custom_perm, created = Permission.objects.get_or_create(
        codename='can_get_time_reports',
        content_type=ContentType.objects.get_for_model(Mechanic, for_concrete_model=False)
    )
    mechanic_group.permissions.add(custom_perm)


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0025_merge_20200408_0939'),
    ]

    operations = [
        migrations.RunPython(update_mechanic_group_perms)
    ]
