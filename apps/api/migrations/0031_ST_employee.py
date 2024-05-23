from django.db import migrations


def add_default_employee_to_employee_works(apps, _):
    EmployeeWorkBlock = apps.get_model('api', 'EmployeeWorkBlock')
    for employee_work in EmployeeWorkBlock.objects.filter(employee__isnull=True):
        employee_work.employee = employee_work.service_ticket.connected_job.mechanics.first()
        employee_work.save(update_fields=['employee'])


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20200213_1327'),
    ]

    operations = [
        migrations.RunPython(add_default_employee_to_employee_works),
    ]
