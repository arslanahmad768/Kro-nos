# Generated by Django 2.2.3 on 2020-01-06 12:42

import apps.time_tracker.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    run_before = [
        ('authentication', '0002_create_default_groups'),
    ]

    dependencies = [
        ('time_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indirecthours',
            options={'permissions': [('can_approve_indirect_hours', 'Can approve Indirect Hours'), ('can_reject_indirect_hours', 'Can reject Indirect Hours')], 'verbose_name': 'Indirect Hours', 'verbose_name_plural': 'Indirect Hours'},
        ),
        migrations.AddField(
            model_name='indirecthours',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Open'), (2, 'Rejected'), (3, 'Approved')], default=1, validators=[apps.time_tracker.model_validators.validate_perm], verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='indirecthours',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='indirecthours',
            name='hours',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Spent Hours'),
        ),
        migrations.AlterField(
            model_name='indirecthours',
            name='notes',
            field=models.CharField(blank=True, max_length=255, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='indirecthours',
            name='time_code',
            field=models.CharField(blank=True, max_length=20, verbose_name='Time Code'),
        )
    ]
