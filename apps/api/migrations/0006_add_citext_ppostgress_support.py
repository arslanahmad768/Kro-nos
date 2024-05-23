from django.contrib.postgres.operations import CITextExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_serviceticket_customer'),
    ]

    operations = [
        CITextExtension()
    ]
