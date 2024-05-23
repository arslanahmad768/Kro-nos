import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from parameterized import parameterized

from apps.authentication.tests.factories import (
    AdminFactory, BillerFactory, MechanicFactory, ManagerFactory, SuperuserFactory
)

from ..factories import LocationFactory, CustomerFactory, JobFactory
from ...views import CustomerViewSet


class InitialTestCustomerViewSet(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.admin = AdminFactory()
        cls.biller = BillerFactory()
        cls.mechanic = MechanicFactory()
        cls.manager = ManagerFactory()

        cls.factory = APIRequestFactory()
        cls.view = CustomerViewSet

    def _get_response(self, user, pk=None, **kwargs):
        """Get rendered view response by user"""
        force_authenticate(self.request, user=user)
        response = self.view.as_view(self.schema, **kwargs)(self.request, pk=pk)
        response.render()
        return response


class TestCustomerViewSetCreation(InitialTestCustomerViewSet):

    def setUp(self):
        self.url = reverse('api:customer-list')
        self.schema = {'post': 'create'}
        self.customer_data = {
            'name': 'Customer #1',
            'locations': [{'name': 'UFC'},{'name': 'DZK'}]
        }
        self.request = self.factory.post(
            self.url,
            json.dumps(self.customer_data),
            content_type='application/json'
        )

    @parameterized.expand([
        ('Admin', AdminFactory,),
        ('Superuser', SuperuserFactory,),
    ])
    def test_customer_creating_admin(self, name, user_factory):
        # create Customer as an Admin/Superuser user
        user = user_factory()
        response = self._get_response(user)
        self.assertEqual(response.data['name'], self.customer_data['name'])
        for idx, location in enumerate(response.data['locations']):
            self.assertEqual(location['name'], self.customer_data['locations'][idx]['name'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    @parameterized.expand([
        ('Biller', BillerFactory,),
        ('Manager', ManagerFactory,),
        ('Mechanic', MechanicFactory,),
    ])
    def test_customer_creating(self, name, user_factory):
        # # trying to create Customer as a Biller/Manager/Mechanic user
        user = user_factory()
        response = self._get_response(user)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestCustomerViewSetUpdating(InitialTestCustomerViewSet):

    def setUp(self):
        self.customer = CustomerFactory(locations=(
            LocationFactory(name='AAA'), LocationFactory(name='BBB'), LocationFactory(name='CCC'),)
        )
        self.url = reverse('api:customer-detail', args=[self.customer.id])
        self.schema = {'patch': 'partial_update'}
        self.updating_data = {
            'name': 'Ab Ra Kadabra',
            'locations': [{'name': 'KFC'}]
        }
        self.request = self.factory.patch(
            self.url,
            json.dumps(self.updating_data),
            content_type='application/json'
        )

    @parameterized.expand([
        ('Admin', AdminFactory,),
        ('Superuser', SuperuserFactory,),
    ])
    def test_customer_updating_admin(self, name, user_factory):
        # update Customer as an Admin/Superuser user
        user = user_factory()
        response = self._get_response(user, pk=self.customer.id)
        self.assertEqual(response.data['name'], self.updating_data['name'])
        self.assertEqual(len(response.data['locations']), 4)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @parameterized.expand([
        ('Biller', BillerFactory,),
        ('Manager', ManagerFactory,),
        ('Mechanic', MechanicFactory,),
    ])
    def test_customer_updating(self, name, user_factory):
        # trying to update Customer as a Biller/Manager/Mechanic user
        user = user_factory()
        response = self._get_response(user, pk=self.customer.id)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestCustomerViewSetReadList(InitialTestCustomerViewSet):

    def setUp(self):
        self.customer = CustomerFactory(locations=(
            LocationFactory(name='AAA'), LocationFactory(name='BBB'), LocationFactory(name='CCC'),)
        )
        self.url = reverse('api:customer-list')
        self.request = self.factory.get(self.url)
        self.schema = {'get': 'list'}

    @parameterized.expand([
        ('Admin', AdminFactory,),
        ('Biller', BillerFactory,),
        ('Manager', ManagerFactory,),
        ('Superuser', SuperuserFactory,),
    ])
    def test_customer_list(self, name, user_factory):
        # get Customers list as an Admin/Biller/Manager user
        user = user_factory()
        response = self._get_response(user)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_list_mechanic(self):
        # trying to update Customer as a Mechanic user
        response = self._get_response(self.mechanic)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @parameterized.expand([
        ('Admin', AdminFactory,),
        ('Biller', BillerFactory,),
        ('Manager', ManagerFactory,),
        ('Superuser', SuperuserFactory,),
    ])
    def test_no_pagination(self, name, user_factory):
        for i in range(20):
            CustomerFactory(name=f'Name{i}')
        user = user_factory()
        url = '/api/v1/customers/?all=True'
        response = self.client.get(url, content_type='application/json')
        self.assertNotIn('next', response.data)
        self.assertNotIn('previous', response.data)


class TestCustomerViewSetReadRetrieve(InitialTestCustomerViewSet):

    def setUp(self):
        self.customer = CustomerFactory()
        self.url = reverse('api:customer-detail', args=[self.customer.id])
        self.request = self.factory.get(self.url)
        self.schema = {'get': 'retrieve'}

    @parameterized.expand([
        ('Admin', AdminFactory,),
        ('Biller', BillerFactory,),
        ('Manager', ManagerFactory,),
        ('Superuser', SuperuserFactory,),
    ])
    def test_customer_detail(self, name, user_factory):
        # get Customer by id as an Admin/Biller/Manager user
        user = user_factory()
        response = self._get_response(user, pk=self.customer.id)
        self.assertEqual(response.data['id'], self.customer.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_detail_mechanic(self):
        # trying to get Customer by id as a Mechanic user
        response = self._get_response(self.mechanic, pk=self.customer.id)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestCustomerViewSetRemove(InitialTestCustomerViewSet):

    def setUp(self):
        self.customer = CustomerFactory()
        self.url = reverse('api:customer-detail', args=[self.customer.id])
        self.request = self.factory.delete(self.url)
        self.schema = {'delete': 'destroy'}

    @parameterized.expand([
        ('Admin', AdminFactory, status.HTTP_204_NO_CONTENT,),
        ('Biller', BillerFactory, status.HTTP_403_FORBIDDEN,),
        ('Manager', ManagerFactory, status.HTTP_403_FORBIDDEN,),
        ('Mechanic', MechanicFactory, status.HTTP_403_FORBIDDEN,),
        ('Superuser', SuperuserFactory, status.HTTP_204_NO_CONTENT,),
    ])
    def test_customer_removing(self, name, user_factory, expected_status_code):
        # remove Customer as an Admin/Manager/Biler/Mechanic user
        user = user_factory()
        response = self._get_response(user, pk=self.customer.id)
        self.assertEqual(response.status_code, expected_status_code)

    def test_remove_customer_assigned_to_job(self):
        job = JobFactory(customer=self.customer)
        # remove Customer with related Job as an Admin user
        response = self._get_response(self.admin, pk=self.customer.id)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data[0],
            "You can't remove Customer that already has related Job"
        )


class TestCustomerViewSetRemoveLocation(APITestCase):

    def setUp(self):
        self.location = LocationFactory()
        self.customer = CustomerFactory(locations=(self.location,))
        self.url = reverse('api:customer-remove-location', args=[self.customer.id])
        self.location_data = {'location_id': self.location.id}

    def _get_client_response(self, user):
        self.client.force_login(user)
        response = self.client.patch(
            self.url,
            json.dumps(self.location_data),
            content_type='application/json'
        )
        return response

    @parameterized.expand([
        ('Admin', AdminFactory,),
        ('Superuser', SuperuserFactory,),
    ])
    def test_remove_location_from_customer_admin(self, name, user_factory):
        # remove relation between Customer and Location as an Admin user
        user = user_factory()
        self.assertEqual(self.customer.locations.count(), 1)
        response = self._get_client_response(user)
        self.assertEqual(len(response.data['locations']), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @parameterized.expand([
        ('Mechanic', MechanicFactory,),
        ('Biller', BillerFactory,),
        ('Manager', ManagerFactory,)
    ])
    def test_remove_location_from_customer(self, name, user_factory):
        # remove relation between Customer and Location as a(Mechanic/Biller/Manager) user
        user = user_factory()
        response = self._get_client_response(user)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
