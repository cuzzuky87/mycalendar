from rest_framework import serializers

from calendar_events.models import CalendarEvent
from accounts.models import User

class UserSerializerForCalendarModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','display_name')
        extra_kwargs = {
            'id': {
                'read_only':False,
            }
        }

class CalendarEventReadSerializer(serializers.ModelSerializer):
    user = UserSerializerForCalendarModel()
    class Meta:
        model = CalendarEvent
        fields = '__all__'
        read_only_fields = ('created_at', 'modified_at')
        extra_kwargs = {
            'id':{
                'read_only':True,
            }
        }

class CalendarEventCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = CalendarEvent
        fields = '__all__'
        read_only_fields = ('created_at', 'modified_at')
        extra_kwargs = {
            'id': {
                'read_only':True,
            }
        }
    