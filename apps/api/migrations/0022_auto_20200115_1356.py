# Generated by Django 2.2.3 on 2020-01-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_merge_20200110_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='number',
            field=models.CharField(max_length=50, unique=True, verbose_name='Job number'),
        ),
    ]