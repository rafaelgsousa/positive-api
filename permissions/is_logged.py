from rest_framework.permissions import BasePermission


class IsLogged(BasePermission):
    message = 'You must be logged in to make this request.'
    def has_permission(self, request, view):
        return request.user.logged