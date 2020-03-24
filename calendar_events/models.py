import uuid
from django.db import models

from accounts.models import User

class CalendarEvent(models.Model):
    """Calendar modle """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        dblbooking_query = CalendarEvent.objects.filter(end_at > self.start_at, start_at < self.end_at)
        if dblbooking_query.first() is None:
            super(CalendarEvent, self).save(*args,**kwargs)
        else:
            raise ValueError("The given event is overlaps the time of another one.")
