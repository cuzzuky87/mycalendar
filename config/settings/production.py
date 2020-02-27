from .base import *
import dj_database_url
import django_heroku

django_heroku.settings(locals())

DEBUG = False

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)