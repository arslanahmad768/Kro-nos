from django.db import migrations

from ..group_permissions import update_group_permissions


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_superuser'),
    ]

    operations = [
        migrations.RunPython(update_group_permissions),
    ]
