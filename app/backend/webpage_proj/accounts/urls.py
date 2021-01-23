from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import views as dj_views

from . import views

urlpatterns = [
    # Plain Django
    path('login/', dj_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', dj_views.LogoutView.as_view(), name='logout'),

    # Simple JWT
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # Custom views
    path('logout/blacklist/', views.BlacklistTokenView.as_view(), name='blacklist'),
    path('register/', views.RegisterView.as_view(), name='register'),

]
