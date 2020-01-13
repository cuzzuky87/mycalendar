from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import CalendarEventReadSerializer
from .permissions import IsOwnerOrReadOnly
from calendar_events.models import CalendarEvent

class CalendarEventViewset(viewsets.ModelViewSet):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventReadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
