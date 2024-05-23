# Generated by Django 2.2.3 on 2020-03-19 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0020_auto_20200211_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'permissions': [('can_archive_users', 'Can set Archive Users'), ('can_restore_users', 'Can set Restore Users'), ('can_get_reports', 'Can get Reports'), ('can_editing_approved_st', 'Can editing approved service tickets')], 'verbose_name': 'Admin', 'verbose_name_plural': 'Admins'},
        ),
    ]