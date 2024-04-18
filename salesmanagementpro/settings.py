import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security Key: Use environment variable for security. 
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Debug Mode: Set to False in production.
DEBUG = False

# Allowed Hosts: Add your Azure App Service domain here.
ALLOWED_HOSTS = ['sripalpsm.azurewebsites.net']

# Installed Apps: Add your apps here.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'salesmanagementapp'  # Your custom app
]

# Middleware: Add middleware classes here.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration.
ROOT_URLCONF = 'salesmanagementpro.urls'

# Template configuration.
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
            ],
        },
    },
]

# WSGI application.
WSGI_APPLICATION = 'salesmanagementpro.wsgi.application'

# Database configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sripalpsm-database',               # Name of your PostgreSQL database on Azure
        'USER': 'gfyjzxjjje',                        # Server admin login name
        'PASSWORD': 'Sreepal@2365',                  # Database password
        'HOST': 'sripalpsm-server.postgres.database.azure.com',  # Server name
        'PORT': '5432',                              # PostgreSQL default port is 5432
        'OPTIONS': {
            'sslmode': 'require'                     # Enable SSL mode
        }
    }
}

# Password validation configuration.
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

# Internationalization configuration.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files configuration.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files configuration.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
