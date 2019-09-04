import logging
from django.core.management.base import BaseCommand


# Get an instance of a logger
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': '/var/www/html/pythonproject/django-community/logs/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Log write in a file'

    def handle(self, *args, **kwargs):
        logger.error("Test!!")
        self.stdout.write('Log write in a file')
