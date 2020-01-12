from rest_framework import serializers

from calendar_events.models import CalendarEvent

class CalendarEventReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvent
        fields = '__all__'
        extra_kwargs = {
            'id':{
                'read_only':True,
            }
        }