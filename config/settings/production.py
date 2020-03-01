from .base import *
import dj_database_url
import django_heroku


DEBUG = False

DATABASES = {}
db_from_env = dj_database_url(conn_max_age=600)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())