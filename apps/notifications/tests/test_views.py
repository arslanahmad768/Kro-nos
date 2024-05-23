import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.authentication.tests.factories import ManagerFactory, MechanicFactory
from .factories import ActionFactory


class TestActionViewSet(APITestCase):

    def setUp(self):
        self.mechanic = MechanicFactory()
        ActionFactory.create_batch(3, connected_users=[self.mechanic])
        self.client.force_login(self.mechanic)

    def test_authentication_is_required(self):
        self.client.logout()
        url = reverse('notifications:action-list')
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_action(self):
        url = reverse('notifications:action-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 3)

    def test_viewed_action(self):
        new_action = ActionFactory(connected_users=[self.mechanic])

        url = reverse('notifications:action-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 4)

        url = reverse('notifications:action-viewed-action', args=[new_action.id])
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('is_viewed'), True)

        url = reverse('notifications:action-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 3)

    def test_viewed_action_is_other_user(self):
        manager = ManagerFactory()
        self.client.force_login(manager)
        new_action = ActionFactory(connected_users=[self.mechanic])

        url = reverse('notifications:action-viewed-action', args=[new_action.id])
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data.get('detail'), "Not found.")
