from cqrs.serializers import CQRSSerializer

from menus.serializers import LinkSerializer

from .models import Content, Display, DisplayInstance


class ContentSerializer(CQRSSerializer):
    class Meta:
        model = Content
        fields = (
            'object_id',
        )


class DisplaySerializer(CQRSSerializer):
    content = ContentSerializer(many=True)

    class Meta:
        model = Display
        fields = (
            'blurb',
            'content_set'
        )


class DisplayInstanceSerializer(CQRSSerializer):
    display = DisplayInstance()
    link = LinkSerializer()

    class Meta:
        model = DisplayInstance
        fields = (
            'display',
            'platform',
            'position',
            'link'
        )
