from makegoalsdaily.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Allowed Hosts
ALLOWED_HOSTS = ['*']
