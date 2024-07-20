from django.db import models
from django.utils import timezone

from .course_model import Course


class Planner(models.Model):
    title=models.CharField(max_length=500, blank=True, null=True)
    date=models.DateTimeField(default=timezone.now)
    cover=models.ImageField(upload_to='cover_planner/%Y/%m/%d', blank=True, null=True)
    file=models.FileField(upload_to='file_planner/%Y/%m/%d')
    free=models.BooleanField(default=False)


    def __str__(self):
        return f'Title: {self.title}'