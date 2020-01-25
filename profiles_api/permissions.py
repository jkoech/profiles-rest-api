from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to update their profile"""
        if request.method in permissions.SAFE_METHODS:
            return  True

        return obj.id == request.user.id
