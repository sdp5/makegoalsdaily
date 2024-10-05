from makegoalsdaily.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Allowed Hosts
ALLOWED_HOSTS = ['*']

# HTTPS Forward over Proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True
