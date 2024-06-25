from rest_framework import serializers

from ..models import ImageAlbumMeeting


class ImageAlbumMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageAlbumMeeting
        fields = '__all__'