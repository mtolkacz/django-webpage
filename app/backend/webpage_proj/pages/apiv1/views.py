from rest_framework import generics, permissions
from ..models import Page
from .serializers import PageSerializer


class PageListAPI(generics.ListAPIView):
    queryset = Page.published.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.AllowAny]


class PageDetailAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]


class PageCreateAPI(generics.CreateAPIView):
    queryset = Page.published.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.AllowAny]  # [permissions.IsAdminUser]
