from django.db import migrations


def add_first_user_to_admin_group(apps, _):
    Group = apps.get_model('auth', 'Group')
    User = apps.get_model('authentication', 'User')
    first_user = User.objects.first()
    if first_user is None:
        return None
    all_groups = Group.objects.get(name='Superuser')
    first_user.groups.add(all_groups)
    first_user.is_confirmed_email = True
    first_user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20191129_1410'),
    ]

    operations = [
        migrations.RunPython(add_first_user_to_admin_group),
    ]
