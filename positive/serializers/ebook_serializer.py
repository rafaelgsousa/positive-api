from rest_framework import serializers

from ..models import EBook


class EBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = EBook
        fields = '__all__'