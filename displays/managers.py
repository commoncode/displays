from django.db.models import Q
from django.db.models.query import QuerySet


class ContentQuerySet(QuerySet):

    def enabled(self):

        return self.filter(
            Q(start__isnull=True) | Q(start__lt=Now()),
            Q(end__isnull=True) | Q(end__gt=Now())
            ).order_by('order')
