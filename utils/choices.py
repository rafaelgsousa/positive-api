from django.db import models


class LoginError(models.IntegerChoices):
    ZERO = 0
    UM = 1
    DOIS = 2
    TRES = 3

class typeAccount(models.TextChoices):
    FREE = 'Free'
    BASICO = 'Basico'
    PREMIUM = 'Premium'
    MASTER = 'Master'