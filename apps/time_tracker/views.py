from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
)
from rest_framework import viewsets, status

from .models import IndirectHours, TimeCode
from .serializers import (
    IndirectHoursWriteSerializer, IndirectHoursReadSerializer, TimeCodeReadSerializer
)
from .filters import IndirectHoursFilter
from apps.api.exceptions import DBLockedException
from apps.api.models import DBLockDate
from apps.authentication.permissions import IsAdmin, IsMechanic
from apps.notifications.models import Action
from datetime import datetime


class IndirectHoursViewSet(CreateModelMixin,
                           ListModelMixin,
                           RetrieveModelMixin,
                           UpdateModelMixin,
                           viewsets.GenericViewSet):
    """
    list:

    Indirect Hours endpoint.\n

    create:
    Create a new Indirect Hours instance.

    request example:

        {
            "date": "12-27-2019",
            "hours": 2,
            "time_code": "UTC",
            "notes": "notes",
            "mechanic": "9"
        }

    partial_update:
    Patch a Indirect Hours instance.

    request example:

        {
            "date": "12-27-2019",
            "hours": 9,
            "time_code": "UTC",
            "notes": "notes_new",
            "mechanic": "9"
        }

    Note: Indirect Hour statuses are constants:
        {
            1: "Pending for Approval",
            2: "Rejected",
            3: "Approved"
        }\n
        Filter example: /?status=Open&start_date=09/13/19&end_date=10/13/19&search=WTX&ordering=-date
        Available ordering fields: date, mechanic, hours, time_code, status, notes
        If you want to exclude: /?status!=approved
        If you want to get archived objects: /?is_archive=true
    """

    queryset = IndirectHours.objects.filter(is_archive=False).order_by('-date')
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_class = IndirectHoursFilter
    search_fields = ('mechanic__first_name', 'mechanic__last_name', 'notes',)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_mechanic:
            return queryset.filter(mechanic=user.id)
        elif user.is_manager:
            return queryset.filter(mechanic__manager=user)
        return queryset

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update',):
            return IndirectHoursWriteSerializer
        return IndirectHoursReadSerializer

    @swagger_auto_schema(responses={200: IndirectHoursReadSerializer})
    def create(self, request, *args, **kwargs):
        # print("create method called---", request.data)
        if DBLockDate.objects.get().lock_date and \
            datetime.strptime(request.data['date'], '%m-%d-%Y').date() < DBLockDate.objects.get().lock_date:
            raise DBLockedException()
        return super().create(request, args, kwargs)

    @swagger_auto_schema(responses={200: IndirectHoursReadSerializer})
    def partial_update(self, request, *args, **kwargs):
        print('partial_update()', request.data, kwargs)
        return super().partial_update(request, args, kwargs)

    @action(detail=False, methods=['post'], permission_classes=[IsAdmin])
    def archive_indirect_hours(self, request, pk=None):
        """
        API for the indirect hours archiving logic.
        Send the list of indirect hours id's that you want to archive.
        Request example: { "ids": [1,2] }.
        """
        ids = request.data.get("ids")
        if ids is None or not isinstance(ids, list):
            response = {'ids': [('This field is required. And it should be a list')]}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        error_ids = []
        success_ids = []
        for id in ids:
            try:
                ih_obj = IndirectHours.objects.get(id=id)
                ih_obj.is_archive = True
                ih_obj.save(update_fields=['is_archive'])
                success_ids.append(id)
                Action.objects.filter(
                    connected_object_id=ih_obj.id,
                    object_type=2  # OBJECT_TYPES INDIRECT_HOUR
                ).update(is_viewed=True)
            except (ValueError, IndirectHours.DoesNotExist,):
                error_ids.append(id)
        response = {
            "Successfully archived Indirect Hours (IDs)": success_ids,
            "Failed to archive Indirect Hours (IDs)": error_ids
        }
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[IsAdmin])
    def unarchive_indirect_hours(self, request, pk=None):
        """
        API for the indirect hours unarchive logic.
        Send the list of indirect hours id's that you want to unarchive.
        Request example: { "ids": [1,2] }.
        """
        ids = request.data.get("ids")
        if ids is None or not isinstance(ids, list):
            response = {'ids': [('This field is required. And it should be a list')]}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        error_ids = []
        success_ids = []
        for id in ids:
            try:
                ih_obj = IndirectHours.objects.get(id=id)
                ih_obj.is_archive = False
                ih_obj.save(update_fields=['is_archive'])
                success_ids.append(id)
            except (ValueError, IndirectHours.DoesNotExist,):
                error_ids.append(id)
        response = {
            "Successfully unarchived Indirect Hours (IDs)": success_ids,
            "Failed to unarchive Indirect Hours (IDs)": error_ids
        }
        return Response(response, status=status.HTTP_200_OK)


class TimeCodeViewSet(ListModelMixin, viewsets.GenericViewSet):

    queryset = TimeCode.objects.all()
    pagination_class = None
    permission_classes = (IsAuthenticated, IsAdmin | IsMechanic)
    serializer_class = TimeCodeReadSerializer
