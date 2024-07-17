from rest_framework.permissions import BasePermission
from rest_framework import permissions

class RequestPermissionAny(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False