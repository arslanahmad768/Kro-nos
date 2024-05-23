# Generated by Django 2.2.3 on 2019-12-03 15:41

import django.contrib.postgres.fields.citext
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_add_citext_ppostgress_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=django.contrib.postgres.fields.citext.CICharField(max_length=3, unique=True, verbose_name='Location code name'),
        ),
    ]