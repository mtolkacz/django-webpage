from rest_framework import generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer

from ..models import Entry
from .serializers import EntrySerializer, EntryDetailSerializer


class EntryListAPI(generics.ListAPIView):
    queryset = Entry.published.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.AllowAny]


class EntryDetailAPI(generics.RetrieveAPIView):
    queryset = Entry.published.all()
    serializer_class = EntrySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/detail.html'
    permission_classes = [permissions.AllowAny]


class EntryCommentDetailAPI(generics.RetrieveAPIView):
    queryset = Entry.published.all()
    serializer_class = EntryDetailSerializer
    permission_classes = [permissions.AllowAny]


class EntryCreateAPI(generics.CreateAPIView):
    queryset = Entry.published.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAdminUser]

