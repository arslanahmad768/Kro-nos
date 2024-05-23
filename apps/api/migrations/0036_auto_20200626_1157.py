# Generated by Django 2.2.3 on 2020-06-26 11:57

import django.contrib.postgres.fields.citext
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_merge_20200407_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=django.contrib.postgres.fields.citext.CICharField(max_length=4, unique=True, verbose_name='Location code name'),
        ),
    ]