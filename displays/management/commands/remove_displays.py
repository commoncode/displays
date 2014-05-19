from django.core.management.base import BaseCommand, CommandError

from ...models import DisplayInstance


class Command(BaseCommand):
    help = 'Remove Displays'

    def handle(self, *args, **options):
        print "Removing Display Instances"

        for display in DisplayInstance.objects.all():
            display.links.all().delete()
            display.delete()
