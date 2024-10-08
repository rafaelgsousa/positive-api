from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from ..models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    id = serializers.UUIDField(read_only=True)
    # login_erro = serializers.IntegerField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'email', 'groups', 'phone', 'type_account', 'last_login', 'password', 'login_erro', 'logged', 'score']