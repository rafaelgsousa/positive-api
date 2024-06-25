from rest_framework import serializers

from ..models import VideoCourse


class VideoCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoCourse
        fields = '__all__'