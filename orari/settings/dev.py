from .base import *
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'orari_main',
        'USER': 'orari_main_user',
        'PASSWORD': 'haiducului',
        'HOST': 'localhost',
        'PORT': '',
    }
    }