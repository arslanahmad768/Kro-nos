"""
If you need to change default model permission in Django admin panel
you can add two-tuple to one of the list below.
Permission is two-tuple where first argument is Model and second argument is permission codename.

!!! If you need to apply new changes add migrations for that action !!!
"""
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from apps.api.models import Customer, Location, Job, ServiceTicket
from apps.time_tracker.models import IndirectHours

BILLER_PERMISSIONS = [
    (Customer, ('view_customer')),
    (Location, ('view_location')),
    (Job, ('add_job')),
    (Job, ('view_job')),
    (Job, ('change_job')),
    (Job, ('delete_job')),
    (Job, ('can_set_pending_for_approval_job')),
    (ServiceTicket, ('view_serviceticket')),
    (ServiceTicket, ('change_serviceticket')),
    (ServiceTicket, ('can_reject_service_ticket')),
    (ServiceTicket, ('can_approve_service_ticket')),
    (IndirectHours, ('view_indirecthours')),

]

MANAGER_PERMISSIONS = [
    (Customer, ('view_customer')),
    (Location, ('view_location')),
    (Job, ('add_job')),
    (Job, ('view_job')),
    (Job, ('change_job')),
    (Job, ('delete_job')),
    (Job, ('can_set_pending_for_approval_job')),
    (ServiceTicket, ('add_serviceticket')),
    (ServiceTicket, ('view_serviceticket')),
    (ServiceTicket, ('change_serviceticket')),
    (ServiceTicket, ('can_reject_service_ticket')),
    (ServiceTicket, ('can_approve_service_ticket')),
    (IndirectHours, ('view_indirecthours')),
    (IndirectHours, ('can_reject_indirect_hours')),
    (IndirectHours, ('can_approve_indirect_hours')),
]

MECHANIC_PERMISSIONS = [
    (Job, ('view_job')),
    (ServiceTicket, ('add_serviceticket')),
    (ServiceTicket, ('view_serviceticket')),
    (ServiceTicket, ('can_set_pending_for_approval_service_ticket')),
    # Only main Mechanic can cdo this actions
    (ServiceTicket, ('change_serviceticket')),
    (ServiceTicket, ('add_mechanic_to_service_ticket')),
    (IndirectHours, ('add_indirecthours')),
    (IndirectHours, ('change_indirecthours')),
]


def add_permission_to_group(group, permissions):
    """Add permission to the group"""
    for permission in permissions:
        content_type = ContentType.objects.get_for_model(permission[0])
        permission = Permission.objects.filter(content_type=content_type).get(
            codename=permission[1]
        )
        group.permissions.add(permission)
    return group


def update_group_permissions(apps=None, shema_editor=None):

    all_permissions = Permission.objects.all()

    biller_group = Group.objects.get(name='Biller')
    add_permission_to_group(biller_group, BILLER_PERMISSIONS)

    manager_group = Group.objects.get(name='Manager')
    add_permission_to_group(manager_group, MANAGER_PERMISSIONS)

    mechanic_group = Group.objects.get(name='Mechanic')
    add_permission_to_group(mechanic_group, MECHANIC_PERMISSIONS)

    admin_group = Group.objects.get(name='Admin')
    admin_group.permissions.add(*all_permissions)

    superuser_group = Group.objects.get(name='Superuser')
    # Superuser have all permissions for now.
    # Add DENIED_SUPERUSER_PERMISSIONS list if we will need disable acces to some action
    superuser_group.permissions.add(*all_permissions)

    return None


USER_ROLES = (
    (1, 'Admin',),
    (2, 'Biller',),
    (3, 'Manager',),
    (4, 'Mechanic',),
    (5, 'Superuser',),
)
