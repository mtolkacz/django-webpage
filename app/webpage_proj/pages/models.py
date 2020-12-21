from django.contrib.contenttypes.fields import GenericRelation

from ..comments.models import Comment
from ..core.models import WebpageContentModel, TimeStampedModel


class Page(WebpageContentModel, TimeStampedModel):
    comments = GenericRelation(
        Comment,
    )
