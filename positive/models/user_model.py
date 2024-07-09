from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from utils.choices import LoginError, typeAccount


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field is mandatory')
        email = self.normalize_email(email)     
        user = self.model(email=email, **extra_fields)
        user.password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    id=models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    email=models.EmailField(max_length=50, unique=True, null=False, blank=False)
    phone=models.CharField(max_length=20)
    type_account=models.CharField(max_length=7,choices=typeAccount.choices, default=typeAccount.FREE)
    logged=models.BooleanField(default=False)
    login_erro=models.PositiveIntegerField(choices=LoginError.choices, default=LoginError.ZERO)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        blank=True
    )
    first_name = models.CharField(_("name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=1, default='',blank=True, null=True)
    score = models.IntegerField(default=0)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        try:
            user = CustomUser.objects.filter(pk=self.pk).first()

            # if self.is_superuser and not user and CustomUser.objects.filter(is_superuser=True).first():
            #     raise PermissionDenied(detail='Unauthorized procedure.')

            if not user:
                self.username = self.email
                self.password = make_password(self.password)

            elif user and not user.is_superuser and self.password != user.password:
                self.password = make_password(self.password)

            return super().save(*args, **kwargs)
        except PermissionDenied as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERRO)
        
    def __str__(self):
        return f'Name: {self.username} - email: {self.email} - id: {self.id}'