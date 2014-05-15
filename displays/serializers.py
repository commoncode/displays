from rest_framework import serializers

from cqrs.serializers import CQRSSerializer

from menus.models import Link

from .models import Content, Display, DisplayInstance


class LinkArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Link

    def to_native(self, obj):
        return obj


class ContentSerializer(CQRSSerializer):
    class Meta:
        model = Content
        fields = (
            'object_id',
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
