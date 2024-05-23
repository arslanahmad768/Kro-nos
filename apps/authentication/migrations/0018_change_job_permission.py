from django.contrib.auth.models import Group, Permission
from django.db import migrations


def add_biller_and_manager_change_job_permissions(apps, _):
    change_job = Permission.objects.get(codename='change_job')
    manager_group = Group.objects.get(name='Manager')
    manager_group.permissions.add(change_job)
    biller_group = Group.objects.get(name='Biller')
    biller_group.permissions.add(change_job)


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_user_sent_email_notifications'),
    ]

    operations = [
        migrations.RunPython(add_biller_and_manager_change_job_permissions)
    ]
