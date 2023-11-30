# ___ IMPORTAR BASE INICIO
import os
from .base import *



# ___ INICIO DEBUG
DEBUG = True
# ___ FIN DEBUG

# ___ INICIO SERVIDORES PERMITIDAS

ALLOWED_HOSTS = []
# ___ INICIO RUTAS PERMITIDAS

# ___ INICIO DATABASES
DATABASES= {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': get_secret('HOST'),
        'PORT': get_secret('PORT'),
    }
}

# ___ FIN DATABASES

# ___ INICIO INTERNACIONALIZACION

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
# ___ INICIO INTERNACIONALIZACION


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
CKEDITOR_UPLOAD_PATH = "uploads/"
COMPRESS_PRECOMPILERS = (
    (
        'text/x-scss',
        'django_libsass.SassCompiler'
    ),
)

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
