
from __future__ import absolute_import
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import os
import sys

from pathlib import Path
from unipath import Path
# import pdb; pdb.set_trace()

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

PROJECT_DIR = Path(__file__).ancestor(3)
PROJECT_APPS = Path(__file__).ancestor(2)

sys.path.insert(0, Path(PROJECT_APPS, 'apps'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z14qt2#9^hn&-u8krs3i=$*utn92uzpz=obtsn&itbu8pxh(1l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['techboxtools.herokuapp.com','*']


IMPORT_EXPORT_USE_TRANSACTIONS = True



# Application definition

BASE_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
                
]

MY_APPS = [
    
    'account.apps.AccountConfig',
    'dashboard.apps.DashboardConfig',
    'homeblog.apps.HomeblogConfig',
    'import_export',
    'celery',
    'rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    
]

INSTALLED_APPS = BASE_APPS + MY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'techbox.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dashboard.context_processors.profile_pic',
                'dashboard.context_processors.counter',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'techbox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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





STRIPE_PUBLISHABLE_KEY = 'pk_test_51InH3HSIGdFaPfKJeAX2T6YZHlXlxIXWFddeVXRCerZukAG8JoHCgSB9fFw6PvrgAS5o0i84CAJWBLQ030e4RxXC00SAlWJZIc'
STRIPE_SECRET_KEY = 'sk_test_51InH3HSIGdFaPfKJNdcq0B3iD1xTc2vVlFhzCvY53U24QPDYeE0IpCmoeWMPVs0vof5aTBIfi0Q9h6Wnf8vKTFrl00RaRddpgy'




sentry_sdk.init(
    dsn="https://4974b7cb3e694b07bbc88fc0c8b5b162@o588496.ingest.sentry.io/5739035",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,


    send_default_pii=True
)



CACHE_MIDDLEWARE_SECONDS = 5
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'dashboard_cache',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
   

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }



# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': 'F:/techbox/cache',
         
#     }
# }




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR,"media")
STATIC_ROOT = os.path.join(BASE_DIR,"static")
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# LOGIN_URL='/login/'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "ishwarmandloi25@gmail.com"
EMAIL_HOST_PASSWORD = "serveradmin25@1994"


CELERY_TIMEZONE = "Asia/Kolkata"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 20 * 50



BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
CELERY_IMPORTS = ['dashboard.task']
