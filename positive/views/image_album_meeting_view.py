from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from permissions import DjangoModelPermissionsCustom, IsLogged

from ..models import ImageAlbumMeeting
from ..serializers import ImageAlbumMeetingSerializer


class ImageAlbumMeetingView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissionsCustom, IsLogged]
    serializer_class = ImageAlbumMeetingSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post']
    queryset = ImageAlbumMeeting.objects.all()