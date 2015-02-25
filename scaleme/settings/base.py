
from os.path import dirname, join
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = dirname(dirname(__file__))
APP_DIR = join(ROOT_DIR, 'junction')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zbhyxwg5%b7#*_gufl@!l3!v%p*&q*f-11ch6^o+zvcn6cat4+'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
CORE_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
)

OUR_APPS = (
    'blogger',
)

INSTALLED_APPS = CORE_APPS + THIRD_PARTY_APPS + OUR_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'scaleme.urls'

WSGI_APPLICATION = 'scaleme.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

