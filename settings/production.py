from .base import *

DEBUG = False

TIME_ZONE = 'America/Chicago'

ALLOWED_HOSTS = ['api.kro-nos.com']

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

# Pusher Channels
PUSHER_APP_ID = '953085',
PUSHER_KEY = '4f6a01361fa3b4b73d1f',
PUSHER_SECRET = 'ee8d22a7bad59f9c620c',
PUSHER_CLUSTER = 'us3',
PUSHER_USE_SSL = True

# Pusher Beamns
PUSHER_INSTANCE_ID = '6ac9d209-a26a-4859-98b3-facf9c526ebf'
PUSHER_SECRET_KEY = 'FF0D3F6F64E544D2DF7C0D247F623B88D29374706F89D0D51ABE8FC76D86C596'

# Mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'K&R Operating LLC'
EMAIL_HOST_PASSWORD = 'hy3kLU5IRKYLMKw1skRQEw'

DEFAULT_FROM_EMAIL = 'notifier@kro-nos.com'

# envs from the docker container
FRONT_HOST = os.environ.get('FRONT_HOST', 'https://kro-nos.com')
STATIC_HOST = os.environ.get('STATIC_HOST', 'api.kro-nos.com')
