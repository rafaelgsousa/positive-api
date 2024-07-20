from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from .course_model import Course


class EBook(models.Model):
    title=models.CharField(max_length=500, blank=True, null=True)
    date=models.DateTimeField(default=timezone.now)
    cover=models.ImageField(upload_to='cover_ebook/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    file=models.FileField(upload_to='file_ebook/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    free=models.BooleanField(default=False)


    def __str__(self):
        return f'Title: {self.title}'