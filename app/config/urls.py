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

    # Django admin interface
    path('webpage-admin/', admin.site.urls),

    path('hello/', HelloView.as_view(), name='hello'),

    # Homepage of webpage project
    path(
        route='',
        view=TemplateView.as_view(
            template_name='index.html'
        ),
        name='index'
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
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
                       path('__debug__/', include(debug_toolbar.urls)),
                   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


