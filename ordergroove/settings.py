"""
Django settings for ordergroove project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import random
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'ordergroove/apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!_!s8r72@@b&=8rb%uaty(d*ol$)wxje=xt%xxlg1u72gc(1+('
SITE_ID = 1
LOGIN_URL = '/registration/login/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1',)
MEDIA_VERSION = random.randint(1, 1000000)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    ##############
    # EXTENSIONS #
    ##############
    'django_extensions',
    'debug_toolbar',
    'easy_thumbnails',
    'south',

    ########
    # APPS #
    ########
    'ordergroove',
    'registration',
    'shop',
    'shop.products',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # debug_toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # django
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    "django.core.context_processors.request",

    # custom
    "ordergroove.context_processors.main_context",
    "shop.context_processors.shop_context",
)

ROOT_URLCONF = 'ordergroove.urls'
WSGI_APPLICATION = 'ordergroove.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/html/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "ordergroove/static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/html/media/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_DIR + '/ordergroove/templates/',
)

# email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'username'
# EMAIL_HOST_PASSWORD = 'password'
# DEFAULT_FROM_EMAIL = ''

##########
# CUSTOM #
##########
REGISTRATION = {
    'LOGIN_REDIRECT': 'home',
    'LOGOUT_REDIRECT': 'registration_logout',
    'REGISTER_REDIRECT': 'registration_register_complete',
    'CONFIRM_EMAIL': False,
}

SHOP = {
    'TRACK_INVENTORY': True,
}

##################
# LOCAL SETTINGS #
##################
try:
    from ordergroove.local_settings import *
except ImportError:
    pass

if DEBUG:
    from fnmatch import fnmatch

    class glob_list(list):
        def __contains__(self, key):
            for elt in self:
                if fnmatch(key, elt):
                    return True
            return False

    INTERNAL_IPS = glob_list(['127.0.0.1', '*.*.*.*'])
