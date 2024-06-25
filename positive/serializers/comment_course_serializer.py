from rest_framework import serializers

from ..models import CommentCourse


class CommentCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentCourse
        fields = '__all__'