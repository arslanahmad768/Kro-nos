# Generated by Django 3.2.23 on 2024-02-07 12:45

from django.db import migrations, models
import django.db.models.deletion

def copy_data(apps, schema_editor):
    IndirectHours = apps.get_model('time_tracker', 'IndirectHours')

    for instance in IndirectHours.objects.all():
        instance.mechanic_new.add(instance.mechanic)


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0027_user_manager'),
        ('time_tracker', '0016_merge_20200522_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='indirecthours',
            name='mechanic_new',
            field=models.ManyToManyField(to='authentication.Mechanic', verbose_name='Mechanics'),
        ),
        migrations.RunPython(copy_data),
        migrations.AlterField(
            model_name='indirecthours',
            name='mechanic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechanic', to='authentication.mechanic'),
        ),
    ]
