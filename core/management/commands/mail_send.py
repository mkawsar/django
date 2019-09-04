import os
from django.core.mail import send_mail
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Sending mail service'

    def handle(self, *args, **kwargs):
        send_mail(
            'Test',
            'Test django e-mail send service',
            os.environ.get('EMAIL_HOST_USER'),
            ['kawsar.swe@gmail.com']
        )
