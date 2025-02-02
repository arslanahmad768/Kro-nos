# Generated by Django 2.2.3 on 2020-02-04 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0018_change_job_permission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'permissions': [('can_archive_users', 'Can set Archive Users'), ('can_restore_users', 'Can set Restore Users'), ('can_get_reports', 'Can get Reports')], 'verbose_name': 'Admin', 'verbose_name_plural': 'Admins'},
        ),
    ]
