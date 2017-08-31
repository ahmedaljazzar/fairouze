from .settings import * # pylint: disable=unused-wildcard-import

DEBUG = False

ALLOWED_HOSTS = [
    'www.fairuze.com',
    'fairuze.herokuapp.com',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # NOQA

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
