from datetime import timedelta

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class WebpageContentModel(models.Model):

    class PublishedContentManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(
                pub_date__isnull=False,
            )

    class LatestContentManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(
                created_date__gte=datetime.now() - timedelta(1),
            )

    DRAFT = 1
    PUBLISHED = 2
    OPTIONS = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Published')),
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
        blank=True,
    )
    slug = models.SlugField(
        max_length=250,
        unique_for_date='pub_date'
    )
    status = models.PositiveSmallIntegerField(
        choices=OPTIONS,
        default=DRAFT,
    )

    objects = models.Manager()  # The default manager.
    published = PublishedContentManager()  # The published content manager.
    latest = LatestContentManager()  # Latest content - default over the last day.

    class Meta:
        ordering = (
            '-pub_date',
        )
        abstract = True

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.pub_date and self.status == self.PUBLISHED:
            self.pub_date = timezone.now()

        super(WebpageContentModel, self).save(*args, **kwargs)


class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    modified_date = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
