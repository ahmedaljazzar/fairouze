from .settings import * # pylint: disable=unused-wildcard-import

DEBUG = False

ALLOWED_HOSTS = [
    'www.fairuze.com',
    'fairuze.herokuapp.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('FAIRUZE_DB_NAME', 'fairuze'),
        'USER': os.environ.get('FAIRUZE_DB_USER', 'root'),
        'PASSWORD': os.environ.get('FAIRUZE_DB_PASSWORD', ''),
        'HOST': os.environ.get('FAIRUZE_DB_HOST', ''),
        'PORT': os.environ.get('FAIRUZE_DB_PORT', ''),
        'OPTIONS': {'charset': 'utf8'},
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # NOQA

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
