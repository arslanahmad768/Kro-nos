# Generated by Django 2.2.3 on 2020-02-06 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0009_update_admin_group_perms'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48, unique=True, verbose_name='Time Code')),
            ],
        ),
        migrations.AlterModelOptions(
            name='indirecthours',
            options={'permissions': [('can_approve_indirect_hours', 'Can approve Indirect Hours'), ('can_reject_indirect_hours', 'Can reject Indirect Hours'), ('can_archive_indirect_hours', 'Can set Archive IndirectHours'), ('can_restore_indirect_hours', 'Can set Restore IndirectHours')], 'verbose_name': 'Indirect Hours', 'verbose_name_plural': 'Indirect Hours'},
        ),
        migrations.AlterField(
            model_name='indirecthours',
            name='time_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='time_code', to='time_tracker.TimeCode'),
        ),
    ]
