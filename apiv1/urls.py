from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from .views import CalendarEventViewset

router = routers.DefaultRouter()
router.register('events', CalendarEventViewset)

urlpatterns = [
    path('',include(router.urls)),
]