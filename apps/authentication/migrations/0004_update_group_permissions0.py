"""
This migration updates Group permissions from group_permissions module.
You can reuse it every time you need to change permission in proxy model.
"""
from django.db import migrations

from ..group_permissions import update_group_permissions


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_create_default_permissions'),
    ]

    operations = [
        migrations.RunPython(update_group_permissions),
    ]
