from django.urls import path
from .views import apiv1

app_name = "webpage_proj.pages"

urlpatterns = [
    path(
        route='apiv1/<int:pk>-<str:slug>/',
        view=apiv1.PageDetailAPI.as_view(),
        name='detail',
    ),
    path(
        route='apiv1/',
        view=apiv1.PageListAPI.as_view(),
        name='list',
    ),
    path(
        route='apiv1/create/',
        view=apiv1.PageCreateAPI.as_view(),
        name='create',
    ),
]
