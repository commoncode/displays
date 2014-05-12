from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Display
from .serializers import DisplayInstanceSerializer


class DisplayDocumentCollection(DRFDocumentCollection):
    model = Display
    serializer_class = DisplayInstanceSerializer
    name = 'economica__displays'


mongodb.register(DisplayDocumentCollection())
