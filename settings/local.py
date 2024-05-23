from .base import *

DEBUG = True

# Credentials for superuser created via `manage.py create_dev_superuser`
DEV_SUPERUSER_EMAIL = 'admin@admin.com'
DEV_SUPERUSER_PASSWORD = 'admin123'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'kandr',
#         'USER': 'kandr',
#         'PASSWORD': 'kandr',
#         'HOST': 'localhost',
#         'PORT': 5432,
#         'ATOMIC_REQUESTS': True
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kronos',
        'USER': 'postgres',
        'PASSWORD': 'tiksom',
        'HOST': 'localhost',
        'PORT': 5432,
        'ATOMIC_REQUESTS': True
    }
}

# Mail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST = 'smtp.mandrillapp.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'K&R Operating LLC'
# EMAIL_HOST_PASSWORD = 'hy3kLU5IRKYLMKw1skRQEw'

# DEFAULT_FROM_EMAIL = 'K&R_postmaster_local@kro-nos.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Update with your SMTP server
EMAIL_PORT = 587  # Update with your SMTP server port
EMAIL_USE_TLS = True  # Set to True if your SMTP server requires TLS
EMAIL_HOST_USER = 'masab.akram@tiksom.com'  # Update with your email address
EMAIL_HOST_PASSWORD = 'masab046tik' 
DEFAULT_FROM_EMAIL = 'masab.akram@tiksom.com'


# Pusher Channels
PUSHER_APP_ID = '953083',
PUSHER_KEY = 'ed32d244a8f3ef23a6b1',
PUSHER_SECRET = '7db8eb0c40666b251b07',

# Pusher Beamns
PUSHER_INSTANCE_ID = '6ac9d209-a26a-4859-98b3-facf9c526ebf'
PUSHER_SECRET_KEY = 'FF0D3F6F64E544D2DF7C0D247F623B88D29374706F89D0D51ABE8FC76D86C596'


# envs from the docker container
FRONT_HOST = os.environ.get('FRONT_HOST', 'http://localhost:3000')
#FRONT_HOST = os.environ.get('FRONT_HOST', 'http://127.0.0.1:8000')
STATIC_HOST = os.environ.get('STATIC_HOST', 'http://localhost:8000')

