# Generated by Django 2.2.3 on 2020-01-06 15:32

import apps.time_tracker.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0004_auto_20200106_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indirecthours',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pending for Approval'), (2, 'Rejected'), (3, 'Approved')], default=1, validators=[apps.time_tracker.model_validators.validate_perm], verbose_name='Status'),
        ),
    ]
