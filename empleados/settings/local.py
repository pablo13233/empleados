from pathlib import Path
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'empleados',
        'USER': 'postgres',
        'PASSWORD': '!postgres!',
        'HOST': '190.4.14.18',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.parent / 'static'
]

MEDIA_ROOT =  [
    BASE_DIR.parent / 'media'
]

MEDIA_URL = '/media/'