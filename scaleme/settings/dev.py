from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(ROOT_DIR, 'db.sqlite3'),
    }
}


# Email Settings.
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pymailone@gmail.com'
EMAIL_HOST_PASSWORD = 'nabeelnabeel'
DEFAULT_FROM_EMAIL = 'pymailone@gmail.com'
SERVER_EMAIL = 'pymailone@gmail.com'


# CELERY
BROKER_URL = 'redis://127.0.0.1:6379/0'
BROKER_TRANSPORT = 'redis'
