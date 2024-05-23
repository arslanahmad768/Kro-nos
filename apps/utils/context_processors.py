from django.conf import settings

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


def _https_check(value):
    """
    Simple https check. Add it if there is no such protocol here.
    Suitable for email specifically.
    """
    if not value.startswith('http'):
        return f'https://{value}'
    return value


def get_general_context(request=None):
    """
    Provide default context like os environment variables
    """
    site_host = _https_check(settings.FRONT_HOST)
    logger.debug(f'CLIENT HOST is {site_host}')

    api_host = _https_check(settings.STATIC_HOST)
    logger.debug(f'API HOST is {api_host}')

    return {
        'site_host': site_host,
        'api_host': api_host,
    }
