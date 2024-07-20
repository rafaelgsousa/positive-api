from django.core.validators import FileExtensionValidator
from django.db import models


class Meeting(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateTimeField(blank=True, null=True)
    picture=models.ImageField(upload_to='meeting/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    description=models.CharField(max_length=1000)
    free=models.BooleanField(default=False)


    def __str__(self):
        return f'Title: {self.title}'