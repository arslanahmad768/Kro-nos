# Generated by Django 2.2.3 on 2019-12-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191203_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='title',
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Description'),
        ),
    ]
