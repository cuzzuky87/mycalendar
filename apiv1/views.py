from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CalendarEventReadSerializer
from calendar_events.models import CalendarEvent

class CalendarEventViewset(viewsets.ModelViewSet):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventReadSerializer