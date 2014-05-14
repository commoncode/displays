from random import choice

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from positions.models import Position

from ...factories import DisplayInstanceFactory


class Command(BaseCommand):
    help = 'Create Displays'

    def handle(self, *args, **options):
        print "Creating Display Instances"

        positions = Position.objects.all()

        if not positions.exists():
            call_command('create_positions')

        for i in  range(5):
            DisplayInstanceFactory(position=choice(positions))
            print "Created Display"
