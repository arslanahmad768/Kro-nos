from django.http import HttpResponse
import subprocess
from django.conf import settings
import os

def backup_view(request):
    # Backup database
    dbname = settings.DATABASES['default']['NAME'] 
    backup_file = 'DatabaseBackup.sql'  
    db_user = settings.DATABASES['default']['USER']
    # db_password = settings.DATABASES['default']['PASSWORD']
    os.environ['PGPASSFILE'] = '/home/kro-nos/.pgpass'

    command = f'pg_dump -h localhost -U {db_user} -W -d {dbname} -f {backup_file}'

    try:
        subprocess.run(command, shell=True, check=True)
        with open(backup_file, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{dbname}_backup.sql"'
            return response
    except Exception as e:
        return HttpResponse(f'Error: {e}', status=500)