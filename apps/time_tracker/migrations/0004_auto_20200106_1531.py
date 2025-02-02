# Generated by Django 2.2.3 on 2020-01-06 15:31

import apps.time_tracker.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0003_auto_20200106_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indirecthours',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'PENDING_FOR_APPROVAL'), (2, 'Rejected'), (3, 'Approved')], default=1, validators=[apps.time_tracker.model_validators.validate_perm], verbose_name='Status'),
        ),
    ]
