# Generated by Django 2.2.3 on 2020-10-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_auto_20201015_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeworkblock',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='employeeworkblock',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Time'),
        ),
    ]
