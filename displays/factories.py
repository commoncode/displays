import factory

from django.contrib.webdesign.lorem_ipsum import paragraphs, words

from menus.factories import LinkFactory
from positions.factories import PositionFactory

from faker import Factory


fake = Factory.create()


class DisplayFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'displays.Display'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())


class ContentFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'displays.Content'
    FACTORY_DJANGO_GET_OR_CREATE = ('display', )

    display = factory.SubFactory(DisplayFactory)


class DisplayInstanceFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'displays.DisplayInstance'
    FACTORY_DJANGO_GET_OR_CREATE = ('display', 'position')

    display = factory.SubFactory(DisplayFactory)
    position = factory.SubFactory(PositionFactory)
    platform_id = 1

    @factory.post_generation
    def links(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for link in extracted:
                self.links.add(link)
