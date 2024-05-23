from django.db import migrations


def remove_attachments_without_file(apps, _):
    Attachment = apps.get_model('api', 'Attachment')
    Attachment.objects.filter(file__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20200330_1700'),
    ]

    operations = [
        migrations.RunPython(remove_attachments_without_file),
    ]
