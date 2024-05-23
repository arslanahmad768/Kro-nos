# Generated by Django 2.2.3 on 2020-03-13 15:31
from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from apps.api.models import Job
from apps.time_tracker.models import TimeCode


ADMIN_PERMISSIONS = [
    (Job, ('change_job')),
    (TimeCode, ('add_timecode')),
    (TimeCode, ('view_timecode')),
    (TimeCode, ('change_timecode')),
    (TimeCode, ('delete_timecode')),
]

def update_admin_group_perms(apps, _):
    # add a custom permission to Admin's group
    admin_group = Group.objects.get(name='Admin')
    for codename in ADMIN_PERMISSIONS:
        content_type = ContentType.objects.get_for_model(codename[0])
        custom_perm, created = Permission.objects.get_or_create(
            content_type=content_type,
            codename=codename[1]
        )
        admin_group.permissions.add(custom_perm)

class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0011_auto_20200226_1649'),
    ]

    operations = [
        migrations.RunPython(update_admin_group_perms)
    ]