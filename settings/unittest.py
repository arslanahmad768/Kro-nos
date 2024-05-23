from .base import *  # noqa


# Credentials for superuser created via `manage.py create_dev_superuser`
DEV_SUPERUSER_EMAIL = 'admin@admin.com'
DEV_SUPERUSER_PASSWORD = 'admin123'

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

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Pusher Channels
PUSHER_APP_ID = '953083',
PUSHER_KEY = 'ed32d244a8f3ef23a6b1',
PUSHER_SECRET = '7db8eb0c40666b251b07',

# Pusher Beamns
PUSHER_INSTANCE_ID = 'test-instance-id'
PUSHER_SECRET_KEY = 'test_secret_key'
