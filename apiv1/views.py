from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import CalendarEventReadSerializer,CalendarEventCreateSerializer
from .permissions import IsOwnerOrReadOnly
from calendar_events.models import CalendarEvent

class CalendarEventViewset(viewsets.ModelViewSet):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventReadSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CalendarEventReadSerializer
        elif self.action == 'create':
            return CalendarEventCreateSerializer
        elif self.action == 'retrieve':
            return CalendarEventReadSerializer
        elif self.action == 'update':
            return CalendarEventCreateSerializer

