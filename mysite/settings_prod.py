import os

DEBUG = False

SECRET_KEY = os.environ.get('secret_key')

ALLOWED_HOSTS = ['a-level-test.com', '3.74.228.6']
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('db_name'),
        'USER': os.environ.get('db_user'),
        'PASSWORD': os.environ.get('db_pass'),
        'HOST': os.environ.get('db_host', 'localhost'),
        'PORT': os.environ.get('db_port', '5432'),
    }
}
