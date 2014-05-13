from django.core.management.base import BaseCommand, CommandError

from ...factories import DisplayInstanceFactory


class Command(BaseCommand):
    help = 'Create Displays'

    def handle(self, *args, **options):
        print "Creating Display Instances"

        for i in  range(5):
            DisplayInstanceFactory()
