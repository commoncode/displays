from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import DisplayInstance
from .serializers import DisplayInstanceSerializer


class DisplayInstanceDocumentCollection(DRFDocumentCollection):
    model = DisplayInstance
    serializer_class = DisplayInstanceSerializer
    name = 'economica__displays'


mongodb.register(DisplayInstanceDocumentCollection())
