from rest_framework import serializers

from ..models import VideoMeeting


class VideoMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoMeeting
        fields = '__all__'