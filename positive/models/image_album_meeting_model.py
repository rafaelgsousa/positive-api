from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from .album_meeting_model import AlbumMeeting


class ImageAlbumMeeting(models.Model):
    title=models.CharField(max_length=500, blank=True, null=True)
    date=models.DateTimeField(default=timezone.now)
    picture=models.ImageField(upload_to='album_meetings/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    album=models.ForeignKey(AlbumMeeting, on_delete=models.CASCADE)
    free=models.BooleanField(default=False)


    def __str__(self):
        return f'Title: {self.title}'