from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator.first_name", read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'comment',
            'creator',
            'url',
            'created_date',
            'modified_date',
        )
