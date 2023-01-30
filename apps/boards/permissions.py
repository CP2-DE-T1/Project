from rest_framework import permissions
from django.conf import settings
import jwt
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_revise_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        token = request.headers.get('Authorization').split("")[1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms = settings.ALGORITHM)
        token_user = payload.get('user_id')
        
        return obj.user.id == token_user