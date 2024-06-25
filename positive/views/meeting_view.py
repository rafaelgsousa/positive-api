from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from permissions import DjangoModelPermissionsCustom, IsLogged

from ..models import Meeting
from ..serializers import MeetingSerializer


class MeetingView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissionsCustom, IsLogged]
    serializer_class = MeetingSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post']
    queryset = Meeting.objects.all()