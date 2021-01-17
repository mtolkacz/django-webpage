from rest_framework import serializers
from ..models import Entry


class EntrySerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Entry
        fields = (
            'id',
            'title',
            'creator',
            'excerpt',
            'body',
            'status',
            'url',
        )
