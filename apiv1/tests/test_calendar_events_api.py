from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from calendar_events.models import CalendarEvent


CALENDAR_EVENTS_URL = reverse('calendarevents:calenda')

def sample_calendar_events(user, **params):
    """Create and return a sample events. events can be changed by params"""
    defaults = {
        "title":"block",
        "description":"aaaaa",
        "start_at":"2020-03-25 12:00:00",
        "end_at":"2020-03-25 14:00:00"
    }
    defaults.update(params)
    return CalendarEvent.objects.create(user=user,**defaults)

# class CalendarEventApiTests(TestCase):
#     """Test CalendarEventApi"""

#     def setUp(self):
#         self.client = APIClient()
#         self.user = get_user_model().objects.create_user(
#             "test@test.com",
#             "testpass"
#         )
#         self.client.force_authenticate(self.user)
