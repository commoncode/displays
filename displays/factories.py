import factory

from django.contrib.webdesign.lorem_ipsum import paragraphs, words

from menus.factories import LinkFactory
from positions.factories import PositionFactory

from faker import Factory


fake = Factory.create()


class DisplayFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'displays.Display'

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())


class ContentFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'displays.Content'

    display = factory.SubFactory(DisplayFactory)


class DisplayInstanceFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'displays.DisplayInstance'

    display = factory.SubFactory(DisplayFactory)
    position = factory.SubFactory(PositionFactory)
    link = factory.SubFactory(LinkFactory)
    platform_id = 1
