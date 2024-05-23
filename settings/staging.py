from .base import *

DEBUG = True

# Credentials for superuser created via `manage.py create_dev_superuser`
DEV_SUPERUSER_EMAIL = 'admin@admin.com'
DEV_SUPERUSER_PASSWORD = 'admin123'

ALLOWED_HOSTS = ['api.kandr-staging.atomcream.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT'],
        'ATOMIC_REQUESTS': True
    }
}

# Storage
FILE_UPLOAD_MAX_MEMORY_SIZE = 51380224  # 49 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = None  # Disable request body memory size validation on Django side

# Mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'K&R Operating LLC'
EMAIL_HOST_PASSWORD = 'hy3kLU5IRKYLMKw1skRQEw'

DEFAULT_FROM_EMAIL = 'K&R_postmaster_staging@kro-nos.com'

# Pusher Channels
PUSHER_APP_ID = '953084',
PUSHER_KEY = '979658ac94fabb2a0901',
PUSHER_SECRET = '16c0ef0212d40fedf161',
PUSHER_CLUSTER = 'us3',
PUSHER_USE_SSL = True

# Pusher Beamns
PUSHER_INSTANCE_ID = '6ac9d209-a26a-4859-98b3-facf9c526ebf'
PUSHER_SECRET_KEY = 'FF0D3F6F64E544D2DF7C0D247F623B88D29374706F89D0D51ABE8FC76D86C596'

# envs from the docker container
FRONT_HOST = os.environ.get('FRONT_HOST', 'https://kandr-staging.atomcream.com')
STATIC_HOST = os.environ.get('STATIC_HOST', 'api.kandr-staging.atomcream.com')
