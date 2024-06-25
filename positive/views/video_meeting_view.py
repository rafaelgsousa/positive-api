from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from permissions import DjangoModelPermissionsCustom, IsLogged

from ..models import VideoMeeting
from ..serializers import VideoMeetingSerializer


class VideoMeetingView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissionsCustom, IsLogged]
    serializer_class = VideoMeetingSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = VideoMeeting.objects.all()