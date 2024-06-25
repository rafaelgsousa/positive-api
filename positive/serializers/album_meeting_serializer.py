from rest_framework import serializers

from ..models import AlbumMeeting


class AlbumMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumMeeting
        fields = '__all__'