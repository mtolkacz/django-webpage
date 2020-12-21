from django.conf import settings
from django.db import models


class PublishedWebContentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            pub_date__isnull=False,
        )


class WebpageContentModel(models.Model):
    creator = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(
        max_length=200,
    )
    body = models.TextField()
    pub_date = models.DateTimeField(
        null=True,
    )

    objects = models.Manager()  # The default manager.
    published = PublishedWebContentManager()  # The published content manager.

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    modified_date = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
