from rest_framework import serializers

from apps.api.models import Job, ServiceTicket
from apps.time_tracker.models import IndirectHours
from apps.utils.fields import IntegerChoiceField
from .models import Action


class ActionSerializer(serializers.ModelSerializer):
    object_type = IntegerChoiceField(choices=Action.OBJECT_TYPES)

    class Meta:
        model = Action
        fields = (
            'id', 'creation_date', 'update_date', 'object_type',
            'connected_object_id', 'description',
        )
