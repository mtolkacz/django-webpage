from rest_framework import serializers
from ..models import Page


class PageSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    creator = serializers.CharField(source="creator.first_name", read_only=True)

    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'creator',
            'excerpt',
            'body',
            'url',
            'pub_date',
        )
