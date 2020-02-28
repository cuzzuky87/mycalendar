from .base import *
import dj_database_url
import django_heroku


DEBUG = False

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())