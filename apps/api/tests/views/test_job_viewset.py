import random
from datetime import timedelta
import json
from unittest import skip

from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase

from apps.authentication.tests.factories import (
    ManagerFactory, MechanicFactory, BillerFactory, AdminFactory
)
from apps.notifications.models import Action
from ..factories import CustomerFactory, LocationFactory, JobFactory
from ...models import Job


class TestJobViewSet(APITestCase):

    def setUp(self):
        self.mechanic = MechanicFactory()
        self.manager = ManagerFactory()
        self.job = JobFactory(managers=(self.manager,))
        self.client.force_login(self.manager)
        self.job_data = {
            'status': Job.OPEN,
            'number': random.randint(0, 999999),
            'description': 'Test description',
            'customer': CustomerFactory().id,
            'location': LocationFactory().id,
            'managers': [self.manager.id],
            'mechanics': [self.mechanic.id]
        }

    def test_authentication_is_required(self):
        self.client.logout()
        url = reverse('api:job-list')
        response = self.client.post(url,  content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @skip('Mechanic cannot assigne job now')
    def test_mechanic_has_access_to_job(self):
        url = reverse('api:job-detail', args=[self.job.id])
        response = self.client.post(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_job(self):

        url = reverse('api:job-list')
        response = self.client.post(
            url,
            data=json.dumps(self.job_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('created_by').get('id'), self.manager.id)
        self.assertEqual(response.data.get('status').get('value'), self.job_data.get('status'))
        self.assertEqual(response.data.get('description'), self.job_data.get('description'))
        self.assertEqual(response.data.get('customer').get('id'), self.job_data.get('customer'))
        self.assertEqual(
            response.data.get('managers')[0].get('id'), self.job_data.get('managers')[0]
        )
        self.assertEqual(
            response.data.get('mechanics')[0].get('id'), self.job_data.get('mechanics')[0]
        )
        self.assertEqual(response.data.get('requester'), None)

    def test_update_job(self):
        new_mechanic = MechanicFactory()
        new_manager = ManagerFactory()
        data = {
            'created_by': new_mechanic.id,
            'status': Job.PENDING_FOR_APPROVAL,
            'managers': [new_manager.id],
            'mechanics': [new_mechanic.id]
        }

        url = reverse('api:job-detail', args=[self.job.id])
        response = self.client.patch(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.job.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status').get('value'), data.get('status'))
        self.assertEqual(
            response.data.get('managers')[0].get('id'), data.get('managers')[0]
        )
        self.assertEqual(
            response.data.get('mechanics')[0].get('id'), data.get('mechanics')[0]
        )
        self.assertEqual(response.data.get('requester').get('id'), self.manager.id)

    def test_filters(self):
        job = JobFactory(status=Job.APPROVED, managers=(self.manager,))
        url = reverse('api:job-list')

        response = self.client.get(url, {'status': 'Approved'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 1)

        JobFactory.create_batch(3, managers=(self.manager,))
        today = timezone.now().date().strftime(settings.DATE_FORMAT)
        tomorrow = (timezone.now().date() + timedelta(days=1)).strftime(settings.DATE_FORMAT)
        yesterday = (timezone.now().date() - timedelta(days=1)).strftime(settings.DATE_FORMAT)
        response = self.client.get(url, {'start_date': today})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), Job.objects.count())
        response = self.client.get(url, {'start_date': tomorrow})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 0)

        response = self.client.get(url, {'end_date': tomorrow})
        self.assertEqual(response.data.get('count'), Job.objects.count())
        response = self.client.get(url, {'end_date': yesterday})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 0)

    def test_change_status_by_biller_requester(self):
        biller = BillerFactory()
        manager = ManagerFactory()

        new_job = JobFactory(status=Job.PENDING_FOR_APPROVAL, requester=biller)
        data = {
            'status': Job.APPROVED,
        }
        url = reverse('api:job-detail', args=[new_job.id])

        self.client.force_login(biller)
        response = self.client.patch(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get('non_field_errors')[0],
            'You do not have permissions to set Closed status.'
        )
        self.client.force_login(manager)
        new_job.managers.add(manager)
        response = self.client.patch(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status').get('value'), data.get('status'))

    def test_change_status_by_manager_requester(self):
        biller = BillerFactory()
        manager = ManagerFactory()

        new_job = JobFactory(status=Job.PENDING_FOR_APPROVAL, requester=manager)
        new_job.managers.add(manager)
        data = {
            'status': Job.APPROVED,
        }
        url = reverse('api:job-detail', args=[new_job.id])

        self.client.force_login(manager)
        response = self.client.patch(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get('non_field_errors')[0],
            'You do not have permissions to set Closed status.'
        )
        self.client.force_login(biller)
        response = self.client.patch(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status').get('value'), data.get('status'))

    def test_archived_job(self):
        self.client.force_login(AdminFactory())
        error_id = 10000000
        self.assertFalse(self.job.is_archive)
        all_action = Action.objects.filter(connected_object_id=self.job.id)
        for i in all_action:
            self.assertFalse(i.is_viewed)
        restore_data = {'ids': [self.job.id, error_id]}
        url = reverse('api:job-archive-job')
        response = self.client.post(
            url,
            data=json.dumps(restore_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('Successfully archived Job (IDs)'),
            [self.job.id]
        )
        self.assertEqual(
            response.data.get('Failed to archive Job (IDs)'),
            [error_id]
        )
        new_job = Job.objects.get(id=self.job.id).is_archive
        all_action = Action.objects.filter(connected_object_id=self.job.id)
        for i in all_action:
            self.assertTrue(i.is_viewed)
        self.assertTrue(new_job)

    def test_unarchived_job(self):
        self.client.force_login(AdminFactory())
        error_id = 10000000
        new_job = JobFactory(is_archive=True)
        self.assertTrue(new_job.is_archive)
        restore_data = {'ids': [new_job.id, error_id]}
        url = reverse('api:job-unarchive-job')
        response = self.client.post(
            url,
            data=json.dumps(restore_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('Successfully unarchived Job (IDs)'),
            [new_job.id]
        )
        self.assertEqual(
            response.data.get('Failed to unarchive Job (IDs)'),
            [error_id]
        )
        new_job = Job.objects.get(id=self.job.id).is_archive
        self.assertFalse(new_job)

    def test_archived_job_with_wrong_role(self):
        new_user = ManagerFactory()
        self.client.force_login(new_user)
        id = self.job.id
        url = reverse('api:job-archive-job')
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
