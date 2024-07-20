from django.db import models
from django.utils import timezone


class Course(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateTimeField(default=timezone.now, blank=True, null=True)
    cover=models.ImageField(upload_to='cover_course/%Y/%m/%d')
    file=models.FileField(upload_to='file_course/%Y/%m/%d')
    description=models.CharField(max_length=1000)
    free=models.BooleanField(default=False)


    def __str__(self):
        return f'Title: {self.title}'