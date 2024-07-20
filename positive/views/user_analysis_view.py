from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from permissions import DjangoModelPermissionsCustom, IsLogged

from ..models import WheelUserAnalysis
from ..serializers import WheelUserAnalysisSerializer


class WheelUserAnalysisView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissionsCustom, IsLogged]
    serializer_class = WheelUserAnalysisSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = WheelUserAnalysis.objects.all()

    def create(self, request, *args, **kwargs):
        if str(request.user.id) != request.data['user']:
            return Response({"somente o próprio usuário pode preenche e criar!"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id != instance.user.id:
            return Response({"somente o próprio usuário pode editar!"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)