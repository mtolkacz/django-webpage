from django.contrib import admin

from . import models


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'status',
        'slug',
        'creator',
    )
