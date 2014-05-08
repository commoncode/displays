
from django.db import models
from django.contrib.contenttypes import generic

from cqrs.models import CQRSModel
from entropy.base import (
    AttributeMixin, EnabledMixin, OrderingMixin, TitleMixin
)

from .settings import CONTENT_MODELS


class DisplayInstance(CQRSModel):
    '''
    Displays are reuseable
    '''

    display = models.ForeignKey('Display')
    platform = models.ForeignKey('platforms.Platform')
    position = models.ForeignKey('positions.Position')

    link = models.ForeignKey('menus.Link', blank=True, null=True)


class Display(CQRSModel, AttributeMixin, EnabledMixin, TitleMixin):
    '''
    A Display of Content or Widgets with a given template.

    Some templates accept parameters, such as slideshow duration
    '''
    # title
    # short_title
    # enabled

    blurb = models.TextField(
        blank=True,
        default='')

    def contents(self):
        '''
        Return the content for this display
        '''
        return [
            content for content in
            self.content_set.enabled().prefetch_related('content_object')
            if content.active
        ]


class Content(CQRSModel, OrderingMixin):
    '''
    Content for Display
    '''
    display = models.ForeignKey('Display')

    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        limit_choices_to={'model__in': CONTENT_MODELS },
    )
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
