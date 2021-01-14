from django.urls import path
from .views import apiv1

app_name = "webpage_proj.blog"

urlpatterns = [
    path(
        route='apiv1/<int:pk>/',
        view=apiv1.EntryDetail.as_view(),
        name='detailcreate',
    ),
    path(
        route='apiv1/',
        view=apiv1.EntryList.as_view(),
        name='listcreate',
    ),
]

