from rest_framework import serializers
from ..models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'creator',
            'excerpt',
            'body',
            'status',
        )
