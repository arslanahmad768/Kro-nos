# Generated by Django 2.2.3 on 2019-12-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_update_permissions_for_service_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Active'), (2, 'Archived')], default=1, verbose_name='Status'),
        ),
    ]
