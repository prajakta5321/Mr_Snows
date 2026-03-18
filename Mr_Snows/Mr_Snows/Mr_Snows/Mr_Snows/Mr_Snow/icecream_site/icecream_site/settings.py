"""
Django settings for icecream_site project.
"""

from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# ================== SECURITY ==================

SECRET_KEY = 'on-=6y4v))1w#=p=x+035v#y1vct%h!&(tj*+71(s$o5u0@87b'
DEBUG = True
ALLOWED_HOSTS = []

# ================== APPLICATIONS ==================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'products',
    'cart',
    'accounts',
    'orders'
]

# ================== MIDDLEWARE ==================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ================== URL CONFIG ==================

ROOT_URLCONF = 'icecream_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [BASE_DIR.parent / 'templates'],
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

WSGI_APPLICATION = 'icecream_site.wsgi.application'

# ================== DATABASE (MongoDB) ==================

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mr_snow_db',
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
        }
    }
}

# ================== PASSWORD VALIDATION ==================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================== INTERNATIONALIZATION ==================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ================== STATIC FILES ==================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.parent / 'static']

# ================== AUTH SETTINGS ==================

# settings.py
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/cart/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

