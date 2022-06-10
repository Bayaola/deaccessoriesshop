"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nt=e8$uqsg_4m%zxxhk+11#!9zsl%lh&i_7wv#i0xk@_zbn4*v'

UPLOADCARE = {
    'pub_key': 'f75cd88ed6d003f0123a',
    'secret': 'a47627ebec838ed0efca'
}

# SECURITY WARNING: don't run with debug turned on in production
DEBUG = True

ALLOWED_HOSTS = ['designgenius.herokuapp.com', '127.0.0.1', 'designgenius.biz', '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tinymce',
    # 'hitcount',
    'taggit',
    'crispy_forms',
    'crispy_bootstrap5',
    'mptt',
    'qrcode',
    'pyqrcode',
    'png',
    'ckeditor',
    'ckeditor_uploader',

    'Stores',
    'Accounts',
    'Forums',
    'Basket',
    'Orders',
    'Blogs',
    'Services',
    'Home',


    'pyuploadcare.dj',
    
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # creer une variable globale accessible sur tous les templates
                'Accounts.views.global_params',
                "Basket.context_processors.basket",
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

	
DATABASES = {}
if DEBUG:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    
else:
    # designGenius
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'PASSWORD': 'rMcEBoai0vTEKTuSlVW7HnwOQemeok4-',
    #         'HOST': 'hattie.db.elephantsql.com',
    #         'NAME': 'devsdcak',
    #         'USER': 'devsdcak',
    #     }
    # }
    
    # designGenius2
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'PASSWORD': 'ggx_0fWAxhmVDMwrlp7bURqsYb3OJXhK',
            'HOST': 'hattie.db.elephantsql.com',
            'NAME': 'vacqjqtp',
            'USER': 'vacqjqtp',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# CKEDITOR
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': 1000,
    },
}



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LANGUAGE_SESSION_KEY = '_language'

MEDIA_URL = '/media/'

# Basket session ID
BASKET_SESSION_ID = "basket"

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

AUTH_USER_MODEL = 'Accounts.Account'

LOGIN_URL = 'Accounts:login'
LOGIN_REDIRECT_URL = 'Home:home'
LOGOUT_REDIRECT_URL = 'Home:home'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = 'staticfiles/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

