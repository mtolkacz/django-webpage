from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = True

sentry_sdk.init(
    dsn=get_env_variable('SENTRY_SDK'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    send_default_pii=True
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable('SQL_DATABASE'),
        'USER': get_env_variable('SQL_USER'),
        'PASSWORD': get_env_variable('SQL_PASSWORD'),
        'HOST': get_env_variable('SQL_HOST'),
        'PORT': get_env_variable('SQL_PORT'),
    }
}

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
