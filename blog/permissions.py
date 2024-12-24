# blog/permissions.py

from rest_framework.permissions import BasePermission

class IsAdminOrEditor(BasePermission):
    def has_permission(self, request, view):
        # Check if user has a specific permission or is an admin/editor
        user = request.user
        if user.is_authenticated:
            # You can check for specific roles or permissions
            if user.has_perm('blog.can_create_blog') or user.has_perm('blog.can_edit_blog'):
                return True
            return False
        return False
