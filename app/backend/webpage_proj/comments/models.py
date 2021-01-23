from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..core.models import TimeStampedModel


class Comment(TimeStampedModel):
    PAGE = 'P'
    BLOG = 'B'
    COMMENT_TYPES = (
        (PAGE, _('Page comment')),
        (BLOG, _('Blog comment')),
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
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
