from django.db import migrations


def create_default_groups(apps, _):
    Group = apps.get_model('auth', 'Group')
    Group.objects.create(name='Admin')
    Group.objects.create(name='Biller')
    Group.objects.create(name='Manager')
    Group.objects.create(name='Mechanic')
    Group.objects.create(name='Superuser')


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_groups),
    ]
