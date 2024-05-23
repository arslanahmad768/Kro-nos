from django.db import models
from django.utils.translation import gettext_lazy as _


class Action(models.Model):
    """
    Action model for notifications data.
    """
    JOB = 0
    ST = 1
    INDIRECT_HOUR = 2

    OBJECT_TYPES = (
        (JOB, 'Job',),
        (ST, 'Service Ticket',),
        (INDIRECT_HOUR, 'Indirect Hour',),
    )

    creation_date = models.DateField(_('Creation Date'), auto_now_add=True)
    update_date = models.DateField(_('Update Date'), auto_now=True)

    object_type = models.PositiveSmallIntegerField(_('Object type'), choices=OBJECT_TYPES)
    connected_object_id = models.PositiveIntegerField(_('Connected object id'))
    connected_users = models.ManyToManyField(
        'authentication.User', verbose_name=_('Connected Users')
    )
    description = models.CharField(_('Description'), max_length=255)
    is_viewed = models.BooleanField(_('Is viewed'), default=False)

    def __str__(self):
        return f'Action for {Action.OBJECT_TYPES[self.object_type][1]} #{self.connected_object_id}'
