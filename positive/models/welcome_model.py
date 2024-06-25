from django.db import models
from django.utils import timezone

from .meeting_model import Meeting


class Welcome(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateTimeField(default=timezone.now, blank=True, null=True)
    cover=models.FileField(upload_to='cover_welcome/%Y/%m/%d')
    video=models.FileField(upload_to='video_welcome/%Y/%m/%d')
    description=models.CharField(max_length=1000)


    def __str__(self):
        return f'Title: {self.title}'