from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from ..core.models import TimeStampedModel


class Comment(TimeStampedModel):
    PAGE = 'P'
    BLOG = 'B'
    COMMENT_TYPES = (
        (PAGE, 'Page comment'),
        (BLOG, 'Blog comment'),
    )

    comment = models.CharField(
        max_length=250,
    )
    type = models.CharField(
        max_length=1,
        choices=COMMENT_TYPES,
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
