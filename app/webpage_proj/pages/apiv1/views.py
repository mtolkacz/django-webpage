from rest_framework import generics, permissions
from ..models import Page
from .serializers import PageSerializer


class PageList(generics.ListAPIView):
    queryset = Page.published.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.AllowAny]


class PageDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]

