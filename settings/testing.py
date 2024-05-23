from .base import *

DEBUG = True

# Credentials for superuser created via `manage.py create_dev_superuser`
DEV_SUPERUSER_EMAIL = 'admin@admin.com'
DEV_SUPERUSER_PASSWORD = 'admin123'

ALLOWED_HOSTS = ['api.kandr-test.atomcream.com']

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

# Mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'K&R Operating LLC'
EMAIL_HOST_PASSWORD = 'hy3kLU5IRKYLMKw1skRQEw'

DEFAULT_FROM_EMAIL = 'K&R_postmaster_testing@kro-nos.com'


# Pusher Channels
PUSHER_APP_ID = '953083',
PUSHER_KEY = 'ed32d244a8f3ef23a6b1',
PUSHER_SECRET = '7db8eb0c40666b251b07',

# Pusher Beamns
PUSHER_INSTANCE_ID = 'test-instance-id'
PUSHER_SECRET_KEY = 'test_secret_key'


# envs from the docker container
FRONT_HOST = os.environ.get('FRONT_HOST', 'https://kandr-test.atomcream.com')
STATIC_HOST = os.environ.get('STATIC_HOST', 'api.kandr-test.atomcream.com')
