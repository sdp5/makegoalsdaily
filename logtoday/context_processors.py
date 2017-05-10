
from django.conf import settings


# GLOBAL VARS
APP_NAME = "makeDaily"


def common_template_vars(request):
    """
    Common vars available to all templates
    """
    return {
        'app_name': APP_NAME,
        'app_version': settings.APP_VERSION,
        'user': request.user
    }
