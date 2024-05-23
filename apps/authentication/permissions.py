from rest_framework import permissions
from rest_framework.exceptions import ValidationError


class IsAdminOrOwnUserObjectAccess(permissions.BasePermission):
    """Check that user can update only himself."""

    def has_object_permission(self, request, view, obj):
        """
        Access to the object has an admin or the user who created this object.
        """
        if view.action == 'retrieve' and (request.user == obj or obj.is_superuser):
            return True
        if request.user == obj or request.user.is_admin or request.user.is_superuser:
            return True
        return False


class IsAuthenticated(permissions.IsAuthenticated):
    """
    Add additional layer to check a confirmed email.
    """

    def has_permission(self, request, view, *args, **kwargs):
        return super().has_permission(request, view, *args, **kwargs)


class IsAdmin(permissions.BasePermission):
    """Check that only admin or superuser have access to view."""

    def has_permission(self, request, view, *args, **kwargs):
        return request.user.is_superuser or request.user.groups.filter(name='Admin').exists()


class IsMechanic(permissions.BasePermission):
    """Check that Mechanic have access to view."""

    def has_permission(self, request, view, *args, **kwargs):
        return request.user.groups.filter(name='Mechanic').exists()


class IsExceptTheMechanic(permissions.BasePermission):
    """Everything except the mechanic"""

    def has_permission(self, request, view, *args, **kwargs):
        is_super = request.user.is_superuser
        is_admin = request.user.groups.filter(name='Admin').exists()
        is_biller = request.user.groups.filter(name='Biller').exists()
        is_manager = request.user.groups.filter(name='Manager').exists()
        return is_super or is_admin or is_biller or is_manager
