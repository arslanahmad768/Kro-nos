from datetime import datetime

from django.db import migrations


def set_employee_work_start_and_end_times(apps, _):
    """
    Set start_time and end_time dates same as the related service ticket's date.
    Keep time the same.
    """
    EmployeeWorkBlock = apps.get_model('api', 'EmployeeWorkBlock')
    for start_time_employee_work in EmployeeWorkBlock.objects.filter(start_time__isnull=False):
        date = start_time_employee_work.service_ticket.date
        time = start_time_employee_work.start_time
        start_time_employee_work.start_time = datetime(
            year=date.year, month=date.month, day=date.day, hour=time.hour, minute=time.minute
        )
        start_time_employee_work.save(update_fields=['start_time'])
    for end_time_employee_work in EmployeeWorkBlock.objects.filter(end_time__isnull=False):
        date = end_time_employee_work.service_ticket.date
        time = end_time_employee_work.end_time
        end_time_employee_work.end_time = datetime(
            year=date.year, month=date.month, day=date.day, hour=time.hour, minute=time.minute
        )
        end_time_employee_work.save(update_fields=['end_time'])


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20201015_1800'),
    ]

    operations = [
        migrations.RunPython(set_employee_work_start_and_end_times),
    ]
