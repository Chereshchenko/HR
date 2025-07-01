from rest_framework import permissions

class IsOwnerReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class ResumePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action in ['list', 'retrieve']:
                return True
            if view.action == 'create':
                return request.user.role in ['CANDIDATE', 'ADMIN']
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'ADMIN':
            return True
        if request.user.role == 'HR':
            return request.method in permissions.SAFE_METHODS
        if request.user.role == 'CANDIDATE':
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.user == request.user
        return False