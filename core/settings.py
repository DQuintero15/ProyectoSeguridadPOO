"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

LOGIN_URL = "/accounts/login"

SESSION_COOKIE_AGE = 18000  # 30 minutos

SESSION_SAVE_EVERY_REQUEST = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "AppSeguridad.apps.AppseguridadConfig",
    "landing.apps.LandingConfig",
    "user.apps.UserConfig",
    "FuerzasMilitares.apps.FuerzasmilitaresConfig",
    "phonenumber_field",
    "bootstrap_modal_forms",
    "crispy_forms",
    "crispy_bootstrap5",
    "snowpenguin.django.recaptcha3",
]

# Email sender
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
RECIPIENT_ADDRESS = env("RECIPIENT_ADDRESS")


RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")

RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")

RECAPTCHA_SCORE_THRESHOLD = 0.5

RECAPTCHA_DEFAULT_ACTION = "generic"

RECAPTCHA_LANGUAGE = "es"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "AppSeguridad.context_processors.getDatosGenerales",
                "AppSeguridad.context_processors.getPersonalBatallon",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASS"),
        "HOST": "localhost",
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "/media/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
