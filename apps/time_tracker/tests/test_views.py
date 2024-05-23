import json
from decimal import Decimal

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.authentication.tests.factories import (
    ManagerFactory, MechanicFactory, AdminFactory
)
from apps.notifications.models import Action
from .factories import IndirectHoursFactory, TimeCodeFactory
from ..models import IndirectHours


class TestIndirectHoursViewSet(APITestCase):

    def setUp(self):
        self.indirect_hours = IndirectHoursFactory()
        self.mechanic = MechanicFactory()
        self.client.force_login(self.mechanic)
        self.time_code = TimeCodeFactory()
        self.data = {
            'date': '12-27-2020',
            'hours': 5,
            'time_code': self.time_code.id,
            'notes': 'notes',
            'mechanic': self.mechanic.id
        }

    def test_authentication_is_required(self):
        self.client.logout()
        url = reverse('time_tracker:indirecthours-list')
        response = self.client.post(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_indirect_hours(self):

        url = reverse('time_tracker:indirecthours-list')
        response = self.client.post(
            url,
            data=json.dumps(self.data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data.get('date'), self.data.get('date')
        )
        self.assertEqual(response.data.get('date'), self.data.get('date'))
        self.assertEqual(Decimal(response.data.get('hours')), Decimal(self.data.get('hours')))
        self.assertEqual(response.data.get('time_code').get('id'), self.data.get('time_code'))
        self.assertEqual(response.data.get('notes'), self.data.get('notes'))
        self.assertEqual(response.data.get('mechanic').get('id'), self.data.get('mechanic'))

    def test_create_indirect_hours_by_manager(self):
        self.manager = ManagerFactory()
        self.client.force_login(self.manager)
        url = reverse('time_tracker:indirecthours-list')
        response = self.client.post(
            url,
            data=json.dumps(self.data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_status_by_manager(self):
        self.manager = ManagerFactory()
        self.client.force_login(self.manager)
        data = {
            'status': IndirectHours.REJECTED
        }
        indirect_hours = IndirectHoursFactory(
            status=IndirectHours.PENDING_FOR_APPROVAL
        )
        url = reverse('time_tracker:indirecthours-detail', args=[indirect_hours.id])
        response = self.client.patch(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status').get('value'), data.get('status'))

    def test_archived_indirect_hours(self):
        self.client.force_login(AdminFactory())
        error_id = 10000000
        self.assertFalse(self.indirect_hours.is_archive)
        all_action = Action.objects.filter(connected_object_id=self.indirect_hours.id)
        for i in all_action:
            self.assertFalse(i.is_viewed)
        restore_data = {'ids': [self.indirect_hours.id, error_id]}
        url = reverse('time_tracker:indirecthours-archive-indirect-hours')
        response = self.client.post(
            url,
            data=json.dumps(restore_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('Successfully archived Indirect Hours (IDs)'),
            [self.indirect_hours.id]
        )
        self.assertEqual(
            response.data.get('Failed to archive Indirect Hours (IDs)'),
            [error_id]
        )
        new_ih = IndirectHours.objects.get(id=self.indirect_hours.id).is_archive
        all_action = Action.objects.filter(connected_object_id=self.indirect_hours.id)
        for i in all_action:
            self.assertTrue(i.is_viewed)
        self.assertTrue(new_ih)

    def test_unarchived_indirect_hours(self):
        self.client.force_login(AdminFactory())
        new_ih = IndirectHoursFactory(is_archive=True)
        error_id = 10000000
        self.assertTrue(new_ih.is_archive)
        restore_data = {'ids': [new_ih.id, error_id]}
        url = reverse('time_tracker:indirecthours-unarchive-indirect-hours')
        response = self.client.post(
            url,
            data=json.dumps(restore_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('Successfully unarchived Indirect Hours (IDs)'),
            [new_ih.id]
        )
        self.assertEqual(
            response.data.get('Failed to unarchive Indirect Hours (IDs)'),
            [error_id]
        )
        new_ih = IndirectHours.objects.get(id=self.indirect_hours.id).is_archive
        self.assertFalse(new_ih)

    def test_archived_indirect_hours_with_wrong_role(self):
        new_user = ManagerFactory()
        self.client.force_login(new_user)
        id = self.indirect_hours.id
        url = reverse('time_tracker:indirecthours-archive-indirect-hours')
        restore_data = {'ids': [id]}
        response = self.client.post(
            url,
            data=json.dumps(restore_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.data.get('detail'),
            'You do not have permission to perform this action.'
        )


class TestTimeCodeViewSet(APITestCase):

    def setUp(self):
        self.admin = AdminFactory()

    def test_get_time_codes(self):
        time_codes = TimeCodeFactory.create_batch(4)
        self.client.force_login(self.admin)
        url = reverse('time_tracker:time_code-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(time_codes))
