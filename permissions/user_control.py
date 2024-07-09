from rest_framework import permissions

from positive.models import CustomUser
from positive.serializers import CustomUserSerializer


class UserControl(permissions.BasePermission):
    message = 'Procedimento não autorizado.'
    def has_permission(self, request, view):
        action = view.action
        body = request.data
        if action == 'create':
            if body.get('user') and body.get('user') != request.user.id:
                return False
        if action == 'list':
            user = CustomUser.objects.filter(email=request.user.email).first()
            list_groups = [group.name for group in user.groups.all()]
            serializer = CustomUserSerializer(user).data
            if 'Admin' not in 'Admin' not in list_groups:
                return False
        return True
    
    def has_object_permission(self, request, view, obj):
        user = CustomUser.objects.filter(email=request.user.email).first()
        serializer = CustomUserSerializer(user).data
        list_groups = [group.name for group in user.groups.all()]
        if serializer['id'] != str(obj.id) and 'Admin' not in list_groups:
            return False
        if request.data.get('type_account') and 'Admin' not in list_groups:
            return False            
        return True