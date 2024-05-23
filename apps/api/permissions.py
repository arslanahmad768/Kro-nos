from rest_framework import permissions


class IsHaveAccessToCustomer(permissions.BasePermission):
    """Check that user have permission to customer"""

    def has_permission(self, request, view):

        user = request.user
        # user can update a customer
        if user.has_perm('api.change_customer') and view.action in ['update', 'partial_update']:
            return True
        # user can create a new customer
        if user.has_perm('api.add_customer') and view.action == 'create':
            return True
        # user can access to the list view and object detail information
        if user.has_perm('api.view_customer') and view.action in ['retrieve', 'list']:
            return True
        # user can delete customer
        if user.has_perm('api.delete_customer') and view.action == 'destroy':
            return True
        return False


class CanRemoveCustomerLocation(permissions.BasePermission):
    """Check that user have permission to remove location from customer"""

    def has_permission(self, request, view):
        """
        Remove location from a customer means that we remove relations between the objects.
        That's why this is just  a case of Customer updating action.
        """
        if request.user.has_perm('api.change_customer'):
            return True
        return False
