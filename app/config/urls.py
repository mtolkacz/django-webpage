from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [

    # Django admin interface
    path('webpage-admin/', admin.site.urls),

    # Homepage of webpage project
    path(
        route='',
        view=TemplateView.as_view(
            template_name='index.html'
        ),
        name='index'
    ),

    # Plain Django auth urls, like login, logout, password change
    path(
        'accounts/',
        include('django.contrib.auth.urls'),
    ),

    # All auth social media authentication
    path(
        'accounts/',
        include('allauth.urls'),
    ),

    # Custom user accounts urls, like signup
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


