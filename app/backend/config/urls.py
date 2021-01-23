from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloView(APIView):
    """
    Hello World view - testing purposes
    """

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


urlpatterns = [

    # Homepage of webpage project
    path(
        route='',
        view=TemplateView.as_view(
            template_name='index.html'
        ),
        name='index'
    ),

    path('hello/', HelloView.as_view(), name='hello'),

    # Blog app
    path(
        'blog/',
        include(('webpage_proj.blog.urls', 'blog'), namespace='blog')
    ),

    # Pages app
    path(
        'pages/',
        include(('webpage_proj.pages.urls', 'pages'), namespace='pages')
    ),

    # All auth social media authentication
    path(
        'accounts/',
        include('allauth.urls'),
    ),

    # Custom user accounts urls, like signup
    # Django login/logout views
    # DRF Simple JWT (obtain, refresh token)
    path(
        'accounts/',
        include(('webpage_proj.accounts.urls', 'accounts'), namespace='accounts')
    ),

    # Django admin interface
    path('webpage-admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
                       path('__debug__/', include(debug_toolbar.urls)),
                   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


