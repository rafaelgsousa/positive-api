from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from .user_model import CustomUser


class WheelUserAnalysis(models.Model):
    date=models.DateTimeField(default=timezone.now, blank=True, null=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    love=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    free=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    forgive=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    spiritualize=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    undertake=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    innovate=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    move=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    transform=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    meditate=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    take_selfresponsabbility=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    organize=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    celebrate=models.PositiveIntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])

    def __str__(self):
        return f'Title: {self.user}'