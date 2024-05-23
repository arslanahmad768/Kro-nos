# Generated by Django 2.2.3 on 2019-12-27 15:56

import apps.api.model_validators
import apps.api.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20191227_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('file', models.FileField(upload_to=apps.api.utils.get_file_attachment_path, validators=[apps.api.model_validators.validate_attachment_file_type], verbose_name='File')),
                ('service_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='api.ServiceTicket')),
            ],
        ),
    ]
