from django.db import models
from django.utils import timezone

from .course_model import Course


class VideoCourse(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateTimeField(default=timezone.now)
    video=models.FileField(upload_to='video_course/%Y/%m/%d')
    description=models.CharField(max_length=1000, blank=True, null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return f'Title: {self.title}'