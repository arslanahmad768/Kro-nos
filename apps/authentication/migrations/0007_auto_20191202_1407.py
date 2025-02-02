# Generated by Django 2.2.3 on 2019-12-02 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20191129_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biller',
            options={'permissions': [('can_set_pending_for_approval', 'Can set status Pending for Approval')], 'verbose_name': 'Biller', 'verbose_name_plural': 'Billers'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'permissions': [('can_set_pending_for_approval', 'Can set status Pending for Approval')], 'verbose_name': 'Manager', 'verbose_name_plural': 'Managers'},
        ),
    ]
