from random import choice

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from menus.models import Link
from positions.models import Position

from ...factories import DisplayInstanceFactory


class Command(BaseCommand):
    help = 'Create Displays'

    def handle(self, *args, **options):
        print "Creating Display Instances"

        positions = Position.objects.all()

        if not positions.exists():
            call_command('create_positions')

        links = Link.objects.all()

        for i in range(10):
            random_links = []

            for j in range(3):
                random_links.append(choice(links))

            DisplayInstanceFactory(position=choice(positions),
                links=random_links)

            print "Created Display"
