"""
Django ORM cannot change TimeField to DateTimeField with timezone.
So it should be done using raw SQL query.
"""
from django.db import migrations

START_TIME_SQL = """
    ALTER TABLE "api_employeeworkblock"
    ALTER COLUMN "start_time"
    SET DATA TYPE TIMESTAMP WITH TIME ZONE USING 'yesterday'::date + "start_time"
"""
END_TIME_SQL = """
    ALTER TABLE "api_employeeworkblock"
    ALTER COLUMN "end_time"
    SET DATA TYPE TIMESTAMP WITH TIME ZONE USING 'yesterday'::date + "end_time"
"""


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20200626_1157'),
    ]

    operations = [
        migrations.RunSQL(START_TIME_SQL),
        migrations.RunSQL(END_TIME_SQL)
    ]
