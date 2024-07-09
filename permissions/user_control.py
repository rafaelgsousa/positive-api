from rest_framework import permissions

from positive.models import CustomUser
from positive.serializers import CustomUserSerializer


class UserControl(permissions.BasePermission):
    message = 'Procedimento não autorizado.'
    def has_permission(self, request, view):
        action = view.action
        body = request.data
        if action == 'list':
            user = CustomUser.objects.filter(email=request.user.email).first()
            serializer = CustomUserSerializer(user).data
            if 'Admin' not in serializer.groups:
                return False
        return True
    
    def has_object_permission(self, request, view, obj):
        user = CustomUser.objects.filter(email=request.user.email).first()
        serializer = CustomUserSerializer(user).data
        if request.user.id != obj.id and 'Admin' not in serializer.groups:
            return False
        if request.data.get('type_account') and 'Admin' not in serializer.groups:
            return False            
        return True