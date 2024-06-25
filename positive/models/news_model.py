from django.db import models
from django.utils import timezone


class News(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateTimeField(default=timezone.now, blank=True, null=True)
    picture=models.ImageField(upload_to='news/%Y/%m/%d')
    description=models.CharField(max_length=1000)


    def __str__(self):
        return f'Title: {self.title}'