# Generated by Django 2.2.3 on 2019-12-11 14:27

import django.contrib.postgres.fields.citext
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20191209_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='number',
            field=models.CharField(blank=True, max_length=50, verbose_name='Job number'),
        ),
        migrations.AddField(
            model_name='job',
            name='number_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Job number starting point'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=django.contrib.postgres.fields.citext.CICharField(max_length=255, unique=True, verbose_name='Customer name'),
        ),
    ]