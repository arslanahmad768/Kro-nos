from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def update_mechanic_group_perms(apps, _):
    mechanic_group = Group.objects.get(name='Mechanic')
    Permission.objects.filter(group=mechanic_group, codename='change_job').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_change_user_roles_order_in_db'),
    ]

    operations = [
        migrations.RunPython(update_mechanic_group_perms)
    ]
