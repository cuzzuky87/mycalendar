from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import User
from calendar_events.models import CalendarEvent


class CalendarModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="TestPassword")

    def test_title_representation(self):
        event = CalendarEvent(title="meeting")
        self.assertEqual(str(event),event.title)
        