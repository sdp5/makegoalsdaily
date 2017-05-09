from makedaily.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django Debug Toolbar
INSTALLED_APPS += ('debug_toolbar', )
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

INTERNAL_IPS = ('127.0.0.1', )
