"""
Django settings for imis project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--78_@-l9kx)^b(2n95n*vh^bb3v95&zhv&2he5ny@738f07gtz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_platform',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'imis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#AUTHENTICATION

# AUTH_USER_MODEL = "app_platform.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#CORS CONFIG
CORS_ALLOW_ALL_ORIGINS = DEBUG
if not DEBUG:
    #Domain name of our frontend app
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://\w+\.imis\.com$",
    ]
    
#LOGGERS
LOGGING = {
    "version" : 1,
    "disable_existing_loggers" : False,
    "root" : {
        "handlers": ["console"],
        "level" : "DEBUG"
    },
    "formatters": {
        "verbose": {
            "format" : "\033[36m{name}({levelname}): File {pathname}, line {lineno}, in {funcName}:\n{message}\n\033[32mEND [{created}]\033[0m",
            "style" : "{"
        },
        "verbose-debug": {
            "format" : "\033[32m{name}({levelname}): File {pathname}, line {lineno}, in {funcName}:\n\033[33mMESSAGE:{message}\033[0m\n\033[32mEND [{created}]\033[0m",
            "style" : "{"
        }
    },
    "handlers" : {
        "console" : {
            "level" : "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose"
        },
        "console-debug" : {
            "level" : "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose-debug"
        }
    },
    "loggers" : {
        "imis.stdout" : {
            "handlers" : ["console", "console-debug"],
            "propagate" : True
        }
    }
}

