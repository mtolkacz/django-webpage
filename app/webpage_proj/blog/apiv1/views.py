from rest_framework import generics, permissions
from ..models import Entry
from .serializers import EntrySerializer


class EntryList(generics.ListAPIView):
    queryset = Entry.published.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.AllowAny]


class EntryDetail(generics.RetrieveAPIView):
    queryset = Entry.published.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.AllowAny]


class EntryCreate(generics.CreateAPIView):
    queryset = Entry.published.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAdminUser]

