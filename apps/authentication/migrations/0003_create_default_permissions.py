from django.contrib.auth.management import create_permissions
from django.db import migrations


def create_default_permissions(apps, _):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_create_default_groups'),
    ]

    operations = [
        migrations.RunPython(create_default_permissions),
    ]
