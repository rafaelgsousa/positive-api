from rest_framework import serializers

from ..models import Welcome


class WelcomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Welcome
        fields = '__all__'