from rest_framework import permissions


class HasAccessToReports(permissions.BasePermission):
    """Check that user has permission to get reports"""

    def has_permission(self, request, view):
        return request.user.has_perm('authentication.can_get_reports')
