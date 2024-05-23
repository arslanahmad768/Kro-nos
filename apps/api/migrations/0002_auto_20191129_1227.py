# Generated by Django 2.2.3 on 2019-11-29 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceticket',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_service_tickets', to='authentication.Mechanic'),
        ),
        migrations.AddField(
            model_name='serviceticket',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_tickets_as_customers', to='authentication.Manager'),
        ),
        migrations.AddField(
            model_name='serviceticket',
            name='who_called',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='called_service_tickets', to='authentication.Manager'),
        ),
        migrations.AddField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
