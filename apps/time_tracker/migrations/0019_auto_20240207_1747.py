# Generated by Django 3.2.23 on 2024-02-07 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0018_rename_mechanic_indirecthours_mechanic_old'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indirecthours',
            old_name='mechanic_new',
            new_name='mechanic',
        ),
        migrations.RemoveField(
            model_name='indirecthours',
            name='mechanic_old',
        ),
    ]