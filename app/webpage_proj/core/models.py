from django.conf import settings
from django.db import models


class WebpageContentModel(models.Model):

    class PublishedContentManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(
                pub_date__isnull=False,
            )

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    creator = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(
        max_length=200,
    )
    excerpt = models.TextField(
        null=True,
    )
    body = models.TextField()
    pub_date = models.DateTimeField(
        null=True,
    )
    slug = models.SlugField(
        max_length=250,
        unique_for_date='pub_date'
    )
    status = models.CharField(
        max_length=10,
        choices=options,
        default='published',
    )

    objects = models.Manager()  # The default manager.
    published = PublishedContentManager()  # The published content manager.

    class Meta:
        ordering = (
            '-pub_date',
        )
        abstract = True

    def __str__(self):
        return self.title


class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    modified_date = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
