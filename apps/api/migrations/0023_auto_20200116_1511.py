# Generated by Django 2.2.3 on 2020-01-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_serviceticket_reject_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='Is archive'),
        ),
        migrations.AddField(
            model_name='serviceticket',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='Is archive'),
        ),
    ]
