import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'ddasdasdasf#A$SD%^&*A(sdfdasfas$p_%)&#@f%g^gu4xn2'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'PRIMA-BUS.RU',"10.1.193.253"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'name': 'db_name',
        'USER': 'user_name',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [ STATIC_DIR ]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
