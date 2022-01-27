"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import pymysql
pymysql.install_as_MySQLdb()
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-60h2eb$$lh7ge*+u6j6^nrv03e@11po&vfcxfr^jr*ah%4tc01'

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
    'SeasonMall.apps.SeasonmallConfig',
    'common.apps.CommonConfig',
    'stripe',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = ('127.0.0.1')

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seasonmall_db',
        'USER': 'root',
        'PASSWORD': '@rjy153101',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'new' : {
      'ENGINE': 'django.db.backends.mysql',
      'NAME' : 'S_MALLdb',
      'USER' : 'root',
      'PASSWORD' : '@rjy153101',
      'HOST' : 'localhost',
      'PORT' : '3306',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [ #static files directory 위치 설정
  BASE_DIR / 'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#로그인 성공 시 이동하는 URL
LOGIN_REDIRECT_URL = '/'
#로그아웃 시 이동하는 URL
LOGOUT_REDIRECT_URL = '/'

#이미지를 넣기 위해 필요
MEDIA_URL = '/media/' #SeasonMall/media/파일경로로 나타내기
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #MEDIA_ROOT에 파일이 저장됨 (upload_to 경로가 없으면 MEDIA_ROOT의 경로에 저장됨)

#결제를 위해 필요 (stripe 사용)
STRIPE_PUBLIC_KEY = 'pk_test_51KDr9GLvtI4Ww06EqhkEjq8ppEdMNRYhbKzXTCVzAXA1XXoPeFsSw06IM1HHYUDE4j2R2xyuxFhSj2Khn5sd0lv3001M91j9Hr'
STRIPE_SECRET_KEY = 'sk_test_51KDr9GLvtI4Ww06ElzpTUvOjek0eOlNjfOwUExkp3TvOQymt4kcaxheQ4iVZHEXOT73tCx2OfEFItRZlPJLQL5XQ00xlyQn2C6'

#Django Session Timeout Code
SESSION_COOKIE_AGE = 2400
SESSION_SAVE_EVERY_REQUEST = True

AUTH_USER_MODEL = 'SeasonMall.User'