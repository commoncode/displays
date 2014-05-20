from rest_framework import serializers

from cqrs.serializers import CQRSSerializer

from menus.models import Link
from widgets.models import Widget
from widgets.serializers import WidgetSerializer

from .models import Content, Display, DisplayInstance


class ContentObjectRelatedField(serializers.RelatedField):
    def to_native(self, value):
        if isinstance(value, Widget):
            serializer = WidgetSerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data


class LinkArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Link

    def to_native(self, obj):
        return obj


class ContentSerializer(CQRSSerializer):
    content_object = ContentObjectRelatedField()

    class Meta:
        model = Content
        fields = (
            'content_object',
        )


class DisplaySerializer(CQRSSerializer):
    content_set = ContentSerializer(many=True)

    class Meta:
        model = Display
        fields = (
            'blurb',
            'content_set'
        )


class DisplayInstanceSerializer(CQRSSerializer):
    display = DisplaySerializer()
    links = LinkArraySerializer(source='link_ids', read_only=True)

    class Meta:
        model = DisplayInstance
        fields = (
            'display',
            'platform',
            'position',
            'links'
        )
