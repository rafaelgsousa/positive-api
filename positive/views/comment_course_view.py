from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from permissions import DjangoModelPermissionsCustom, IsLogged

from ..models import CommentCourse
from ..serializers import CommentCourseSerializer


class CommentCourseView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissionsCustom, IsLogged]
    serializer_class = CommentCourseSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post']
    queryset = CommentCourse.objects.all()