from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from permissions import DjangoModelPermissionsCustom, IsLogged

from ..models import News
from ..serializers import NewsSerializer


class NewsView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissionsCustom, IsLogged]
    serializer_class = NewsSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post']
    queryset = News.objects.all()