from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from permissions import DjangoModelPermissionsCustom, IsLogged

from ..models import Welcome
from ..serializers import WelcomeSerializer


class WelcomeView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissionsCustom, IsLogged]
    serializer_class = WelcomeSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post']
    queryset = Welcome.objects.all()