from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH", "DELETE")

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if obj.author == request.user:
            return True

        if request.method not in self.edit_methods:
            return True
        return False


class FollowPermission(permissions.BasePermission):
    allowed_methods = ("GET", "POST")

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.method in self.allowed_methods:
            return True
