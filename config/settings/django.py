import os
from datetime import timedelta
from config.settings.env import env, BASE_DIR


os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = ['*']

print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")

CSRF_TRUSTED_ORIGINS = env.list('DJANGO_CSRF_TRUSTED_ORIGINS', [])
CORS_ALLOW_ALL_ORIGINS = True

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
DJANGO_ALLOW_ASYNC_UNSAFE = True

CORS_ORIGIN_WHITELIST = [
    'https://mu.daark-team.ru',
    'http://localhost:3000'
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'accounts.apps.AccountsConfig',
    'files.apps.FilesConfig',
    'storages',
]

THIRD_PARTY_APPS = [
    "rest_framework",
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
    'social_django',
    'corsheaders',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'accounts.middleware.custom_auth_middleware.CustomAuthenticationMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.int('DB_PORT'),
    }
}

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

LANGUAGE_CODE = env.str('DJANGO_LANGUAGE_CODE', 'ru-ru')

TIME_ZONE = env.str('DJANGO_TIME_ZONE', 'Europe/Moscow')

USE_I18N = True

USE_TZ = True

STATIC_URL = env.str('DJANGO_STATIC_URL', default='/static/')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_OAUTH_CLIENT_ID = env.str('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
GOOGLE_OAUTH_CLIENT_SECRET = env.str('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

YANDEX_OAUTH_CLIENT_ID = env.str('SOCIAL_AUTH_YANDEX_OAUTH2_KEY')
YANDEX_OAUTH_CLIENT_SECRET = env.str('SOCIAL_AUTH_YANDEX_OAUTH2_SECRET')


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',  # Google OAuth2
    'social_core.backends.yandex.YandexOAuth2',  # Yandex OAuth2
    'django.contrib.auth.backends.ModelBackend',  # Стандартная аутентификация
)

SOCIAL_AUTH_YANDEX_OAUTH2_REDIRECT_URI = 'http://mu.daark-team.ru/auth/complete/yandex-oauth2/'
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://mu.daark-team.ru/auth/complete/google-oauth2/'
LOGIN_REDIRECT_URL = "/accounts/social-login/"


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',  # This ensures the UID is extracted.
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)


SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['openid', 'email', 'profile']
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['id', 'email', 'name']
SOCIAL_AUTH_YANDEX_OAUTH2_SCOPE = ['login:email', 'login:info']
SOCIAL_AUTH_YANDEX_OAUTH2_EXTRA_DATA = ['id', 'email']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
    'x-requested-with',
    'accept',
    'origin',
]

EMAIL_BACKEND=env.str('EMAIL_BACKEND')
EMAIL_HOST=env.str('EMAIL_HOST')
EMAIL_PORT=env.int('EMAIL_PORT')
EMAIL_USE_TLS=env.str('EMAIL_USE_TLS')
EMAIL_HOST_USER=env.bool('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env.str('EMAIL_HOST_PASSWORD')