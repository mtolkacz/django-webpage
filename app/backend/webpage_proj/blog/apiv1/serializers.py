from rest_framework import serializers
from ..models import Entry
from ...comments.serializers import CommentSerializer


class EntrySerializer(serializers.ModelSerializer):
    url = serializers.URLField(
        source='get_absolute_url',
        read_only=True,
    )
    creator = serializers.CharField(
        source="creator.first_name",
        read_only=True,
    )
    pub_date = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S',
    )

    class Meta:
        model = Entry
        fields = (
            'id',
            'title',
            'creator',
            'excerpt',
            'body',
            'url',
            'pub_date',
        )


class EntryDetailSerializer(EntrySerializer):
    comments = CommentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Entry
        fields = (
            'id',
            'title',
            'creator',
            'excerpt',
            'comments',
            'body',
            'url',
            'pub_date',
        )
