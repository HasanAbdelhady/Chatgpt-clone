from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret (You can use .env to add it)!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get("DEBUG") == "True" else False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',
    'users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'chatgpt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
            BASE_DIR / "chat"
        ],
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

WSGI_APPLICATION = 'chatgpt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
AUTH_USER_MODEL = 'users.CustomUser'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Add these settings for authentication
LOGIN_URL = 'login'  # Name of our login URL pattern
LOGIN_REDIRECT_URL = 'chat'  # Where to redirect after successful login
LOGOUT_REDIRECT_URL = 'login'  # Where to redirect after logout


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JWT settings loaded from environment variables
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRE_MINUTES"))
JWT_REFRESH_TOKEN_EXPIRE_MINUTES = int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRE_MINUTES"))
