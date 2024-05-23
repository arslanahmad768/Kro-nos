from django.db import migrations


def create_settings_instance(apps, _):
    Settings = apps.get_model('api', 'Settings')
    Settings.objects.create()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_settings'),
    ]

    operations = [
        migrations.RunPython(create_settings_instance),
    ]
