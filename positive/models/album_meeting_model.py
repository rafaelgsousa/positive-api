from django.db import models
from django.utils import timezone

from .meeting_model import Meeting


class AlbumMeeting(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateTimeField(default=timezone.now, blank=True, null=True)
    meeting=models.ForeignKey(Meeting, on_delete=models.CASCADE)


    def __str__(self):
        return f'Title: {self.title}'