from django.urls import path
from .views import apiv1

app_name = "webpage_proj.blog"

urlpatterns = [
    path(
        route='apiv1/<int:pk>-<str:slug>/',
        view=apiv1.EntryDetailAPI.as_view(),
        name='detail',
    ),
    path(
        route='test/apiv1/<int:pk>-<str:slug>/',
        view=apiv1.EntryCommentDetailAPI.as_view(),
        name='detail',
    ),
    path(
        route='apiv1/',
        view=apiv1.EntryListAPI.as_view(),
        name='list',
    ),
    path(
        route='apiv1/create/',
        view=apiv1.EntryCreateAPI.as_view(),
        name='create',
    ),
]

