from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


class Welcome(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateTimeField(default=timezone.now, blank=True, null=True)
    cover=models.FileField(upload_to='cover_welcome/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    video=models.FileField(upload_to='video_welcome/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    description=models.CharField(max_length=1000)


    def __str__(self):
        return f'Title: {self.title}'
