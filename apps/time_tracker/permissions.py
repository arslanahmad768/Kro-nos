from rest_framework import permissions


class IsManager(permissions.BasePermission):
    """Check that only Manager or superuser have access to view."""

    def has_permission(self, request, view, *args, **kwargs):
        return request.user.is_superuser or request.user.groups.filter(name='Manager').exists()
