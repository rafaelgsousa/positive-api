from django.contrib.auth.hashers import check_password
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from permissions import (DjangoModelPermissionsCustom, IsAuthenticatedCustom,
                         IsLogged, UsersControl)
from utils import choices

from ..models import CustomUser
from ..serializers import CustomUserSerializer


class CustomUserView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissionsCustom, IsLogged]
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post']
    queryset = CustomUser.objects.all()

    def get_permissions(self):
        if self.action in ['login']:
            return []
        elif self.action in ['logout']:
            return [IsAuthenticated(), IsLogged()]
        else:
            return [permission() for permission in self.permission_classes]
    
    def get_queryset(self):
        cache.clear()
        return super().get_queryset()

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = CustomUser.objects.filter(email=email).first()

        if not user:
            return Response(
                {
                    'message': 'User not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        try:          
            user_serialize = CustomUserSerializer(user).data
            if user_serialize['login_erro'] >= 3:
                raise PermissionDenied(detail='error: Account blocked due to excessive login errors. Contact an administrator.')
            
            if not user.is_active:
                raise PermissionDenied(detail='error: User is inactive.')
        
            if check_password(password, user.password):

                token = RefreshToken.for_user(user)

                if user.login_erro > 0:
                    user.login_erro = choices.LoginError.ZERO
                    user.save(update_fields=list(['login_erro']))

                user.logged = True
                user.save(update_fields=list(['logged']))

                data = CustomUserSerializer(user).data
                data['unit_name'] = user.unit.name if user.unit else user.unit
                data['agency_name'] = user.agency.name if user.agency else user.agency
                data['role_name'] = user.role.name if user.role else user.role
                data['groups'] = [group.name for group in user.groups.all()] if len(user.groups.all()) else user.groups.all()

                return Response(
                    {
                        'token': str(token.access_token),
                        'user': data
                    },
                    status=status.HTTP_200_OK
                )
            else:
                user.login_erro += 1
                user.save(update_fields=list(['login_erro']))

                if user.login_erro >= 3:
                    raise PermissionDenied(detail='error: Account blocked due to excessive login errors. Contact an administrator.')
                else:
                    return Response(
                        {
                            'error': 'Incorrect password or email. Three login errors lead to account lockout'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except PermissionDenied as e:
            return Response({'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(f'Unexpected error during login: {str(e)}')
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request, *args, **kwargs):
        try:
            date_now = timezone.now()
            instance = get_object_or_404(CustomUser, pk=request.user.id)
            serializer = self.get_serializer(instance, data={"last_login": date_now,"logged": False}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    'user': instance.email,
                    'message': 'logout'
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)