# _______________ INICIO LIBRERIAS USADAS
# Librerias usadas por Django
import os
from unipath import Path
import json
# _______________ FIN LIBRERIAS USADAS

# _______________ INICIO BASE DEL PROYECTO
BASE_DIR = Path(__file__).ancestor(3)
# _______________ INICIO BASE DEL PROYECTO

with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)



# _______________ INICIO SECRECT KEY
SECRET_KEY = get_secret('SECRET_KEY')

# _______________ FIN SECRECT KEY

# _______ INICIO APPS
MY_APPS =(
    'applications.city',
    'applications.country',
    'applications.countrylanguage',
    'applications.language',
    'applications.townhall',
)
DJANGO_APPS =(
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_APPS =(
    'compressor',
    'rest_framework',
)
INSTALLED_APPS = MY_APPS + DJANGO_APPS + THIRD_APPS
# _______ FIN APPS

#_________ INICIO MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#_________ FIN MIDDLEWARE

#_________ INICIO ROOT_URLCONF

ROOT_URLCONF = 'abdpro.urls'
#_________ FIN ROOT_URLCONF

#_________ INICIO TEMPLATES

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#_________ FIN TEMPLATES

#_________ INICIO WSGI_APPLICATION

WSGI_APPLICATION = 'abdpro.wsgi.application'
#_________ FIN WSGI_APPLICATION



#_________ INICIO AUTH_PASSWORD_VALIDATORS

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
#_________ FIN AUTH_PASSWORD_VALIDATORS


#_________ INICIO DEFAULT_AUTO_FIELD

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#_________ FIN DEFAULT_AUTO_FIELD
