from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from .meeting_model import Meeting


class VideoMeeting(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateTimeField(default=timezone.now)
    video=models.FileField(upload_to='video_meeting/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    description=models.CharField(max_length=1000)
    meeting=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    free=models.BooleanField(default=False)


    def __str__(self):
        return f'Title: {self.title}'