# Generated by Django 2.2.3 on 2020-01-15 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0005_auto_20200106_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indirecthours',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 1, 15, 10, 1, 58, 267586, tzinfo=utc), verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indirecthours',
            name='hours',
            field=models.PositiveIntegerField(default=1, verbose_name='Spent Hours'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indirecthours',
            name='notes',
            field=models.CharField(max_length=255, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='indirecthours',
            name='time_code',
            field=models.CharField(max_length=20, verbose_name='Time Code'),
        ),
    ]
