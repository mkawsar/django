from django.utils import timezone
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Display current time'

    def handle(self, *args, **options):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
