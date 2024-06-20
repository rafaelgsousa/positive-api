from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from ..models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    id = serializers.UUIDField(read_only=True)
    # login_erro = serializers.IntegerField(read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        
    def validate(self, data):
        if self.context["view"].action == 'create':
            required_fields = ['first_name', 'last_name', 'email', 'password']
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                raise serializers.ValidationError({'error': f'The following fields are required: {", ".join(missing_fields)}'})
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)