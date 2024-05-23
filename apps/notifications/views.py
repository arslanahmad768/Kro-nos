from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import viewsets, status

from .models import Action
from .serializers import ActionSerializer


class ActionViewSet(ListModelMixin, viewsets.GenericViewSet):
    """
    list:

    Pusher Beams usage documentation:

    1. Send GET request to url:

            /api/v1/auth/beams_auth/

    2. Receive Pusher Beams token
    3. Using received token connect your mobile device
    4. In case of checking/pressing this notification, send a request to url:

            /api/v1/notifications/{action.id}/viewed_action/

    Trigger events for push and email notification:
    1. Service ticket has been Approved
    2. Service ticket has been Rejected
    3. User has been assigned to Job and only if user is mechanic

    Trigger events for email notification:
    1. Job has been closed
    2. Job has been rejected
    3. ST has been closed
    4. Indirect Hours have been submitted

    Action endpoint.\n
        Note: Action object_type:
            {
                1: "JOB",
                2: "ST",
                3: "INDIRECT_HOUR"
            }\n
    request example:

        {
            "id": 2,
            "creation_date": "2020-01-21",
            "update_date": "2020-01-21",
            "object_type": {
                "value": 1,
                "name": "Service Ticket"
            },
            "connected_object_id": 1,
            "description": "Service Ticket"
        }
    """
    queryset = Action.objects.filter(is_viewed=False).order_by('id')
    serializer_class = ActionSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        return queryset.filter(connected_users=user.id)

    @action(detail=True, methods=['patch'])
    def viewed_action(self, request, pk=None):
        """
        Update Action is_viewed.

        url example:

            /api/v1/notifications/{action.id}/viewed_action/

        """
        notifications = get_object_or_404(
            Action.objects.filter(connected_users=self.request.user.id), pk=pk
        )
        notifications.is_viewed = True
        notifications.save()
        return Response({'is_viewed': True}, status=status.HTTP_200_OK)
