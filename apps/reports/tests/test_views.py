from datetime import datetime, timezone, timedelta
import json

from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase

from apps.api.models import CommonInfo, ServiceTicket
from apps.api.tests.factories import (
    ServiceTicketFactory, JobFactory, BillerFactory,
    AttachmentFactory, EmployeeWorkBlockFactory)
from apps.authentication.tests.factories import AdminFactory, MechanicFactory, ManagerFactory
from apps.time_tracker.tests.factories import IndirectHoursFactory


class TestReportsByServiceTicketsViewSet(APITestCase):

    def setUp(self):
        self.fmt = '%m/%d/%Y'
        self.job = JobFactory()
        self.url = reverse('reports:st_full_report-list')
        self.admin = AdminFactory()
        self.expected_fields = (
            'id', 'status', 'requester', 'approval', 'connected_job', 'employee_works', 'created_by',
            'date', 'unit', 'lease_name', 'county', 'state',
            'customer_po_wo', 'who_called', 'engine_model', 'engine_serial',
            'comp_model', 'comp_serial', 'unit_hours', 'rpm', 'suction', 'discharge1',
            'discharge2', 'discharge3', 'safety_setting_lo1', 'safety_setting_lo2',
            'safety_setting_lo3', 'safety_setting_lo4', 'safety_setting_lo5', 'safety_setting_hi1',
            'safety_setting_hi2', 'safety_setting_hi3', 'safety_setting_hi4', 'safety_setting_hi5',
            'engine_oil_pressure', 'engine_oil_temp', 'compressor_oil_pressure',
            'compressor_oil_temp', 'ts1', 'ts2', 'ts3', 'ts4', 'td1', 'td2', 'td3', 'td4',
            'cylinder_temperature_hi1', 'cylinder_temperature_hi2', 'cylinder_temperature_hi3',
            'cylinder_temperature_hi4', 'exhaust_temperature_l', 'exhaust_temperature_r',
            'exhaust_temperature_hi', 'manifold_temperature_l', 'manifold_temperature_r',
            'manifold_temperature_hi', 'manifold_pressure_l', 'manifold_pressure_r',
            'manifold_pressure_hi1', 'manifold_pressure_hi2', 'lo_hi', 'jacket_water_pressure',
            'mmcfd', 'aux_temp', 'hour_meter_reading', 'what_was_the_call', 'what_was_found',
            'what_was_performed', 'future_work_needed', 'additional_notes',
            'customer_signature', 'customer_printed_name', 'reject_description',
            'submitted_for_approval_timestamp', 'approved_timestamp',
            'mileage', 'employee', 'hotel', 'per_diem',
        )

    def test_missing_parameters(self):
        self.client.force_login(self.admin)

        response = self.client.get(
            self.url, content_type='application/json', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        msg = "Both 'start_date' and 'end_date' parameters are required"
        self.assertEqual(response.data[0], msg)

    def test_date_overlap(self):
        self.client.force_login(self.admin)

        creation_date = datetime.now(timezone.utc)

        start_date = datetime.strftime(creation_date + timedelta(days=7), self.fmt)
        end_date = datetime.strftime(creation_date, self.fmt)
        params = {
            'start_date': start_date,
            'end_date': end_date
        }

        response = self.client.get(
            self.url, params, content_type='application/json', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0], 'Start date can not be ahead of End date')

    def test_normal_response(self):
        self.client.force_login(self.admin)

        creation_date = datetime.now(timezone.utc)
        requester = BillerFactory()

        self.service_ticket = ServiceTicketFactory(
            connected_job=self.job,
            date=creation_date,
            creation_date=creation_date,
            status=CommonInfo.APPROVED,
            requester=requester,
        )

        start_date = datetime.strftime(creation_date - timedelta(days=7), self.fmt)
        end_date = datetime.strftime(creation_date, self.fmt)
        params = {
            'start_date': start_date,
            'end_date': end_date
        }

        response = self.client.get(
            self.url, params, content_type='application/json', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_service_ticket_fields(self):
        self.client.force_login(self.admin)

        creation_date = datetime.now(timezone.utc)
        requester = BillerFactory()

        self.service_ticket = ServiceTicketFactory(
            connected_job=self.job,
            date=creation_date,
            creation_date=creation_date,
            status=CommonInfo.APPROVED,
            requester=requester,
        )

        ewb = EmployeeWorkBlockFactory(service_ticket_id=self.service_ticket.id)
        self.service_ticket.employee_works.set([ewb])

        start_date = datetime.strftime(creation_date - timedelta(days=7), self.fmt)
        end_date = datetime.strftime(creation_date, self.fmt)
        params = {
            'start_date': start_date,
            'end_date': end_date
        }

        response = self.client.get(
            self.url, params, content_type='application/json', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        result = response.data[0]

        # checking top-level fields
        result_fields = set(result.keys())
        mandatory_fields = set(self.expected_fields)
        self.assertSetEqual(result_fields, mandatory_fields)

        # checking nested fields
        self.assertTrue(result.get('status').get('name'))

        result_fields_requester = set(result.get('requester'))
        mandatory_fields_requester = set(['first_name', 'last_name'])
        self.assertSetEqual(result_fields_requester, mandatory_fields_requester)

        result_fields_connected_job = set(result.get('connected_job'))
        mandatory_fields_connected_job = set(['id', 'status', 'number', 'customer', 'location'])
        self.assertSetEqual(result_fields_connected_job, mandatory_fields_connected_job)

        result_fields_employee_works = set(result.get('employee_works')[0])
        mandatory_fields_employee_works = set(['id', 'start_time', 'end_time', 'mileage', 'hotel', 'per_diem', 'hours_worked', 'employee'])
        self.assertSetEqual(result_fields_employee_works, mandatory_fields_employee_works)

        result_fields_created_by = set(result.get('created_by'))
        mandatory_fields_created_by = set(['first_name', 'last_name'])
        self.assertSetEqual(result_fields_created_by, mandatory_fields_created_by)

        self.assertTrue(result.get('state').get('name'))


class TestIndirectHoursViewSet(APITestCase):

    def setUp(self):
        self.indirect_hours = IndirectHoursFactory()
        self.mechanic = MechanicFactory()
        self.admin = AdminFactory()
        self.client.force_login(self.admin)

    def test_list_fields(self):
        start_date = (self.indirect_hours.date - timedelta(days=1)).strftime(settings.DATE_FORMAT)
        end_date = (self.indirect_hours.date + timedelta(days=1)).strftime(settings.DATE_FORMAT)
        url = f'/api/v1/reports/user_hours/?start_date={start_date}&end_date={end_date}'
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # first element should be with REG time_code
        self.assertEqual(response.data[0].get('hours')[0].get('time_code'), 'REG')
        self.assertEqual(
            response.data[0].get('hours')[1].get('hours'), self.indirect_hours.hours
        )
        self.assertEqual(
            response.data[0].get('hours')[1].get('time_code'), self.indirect_hours.time_code.name
        )
        self.assertEqual(
            response.data[0].get('hours')[1].get('first_name'),
            self.indirect_hours.mechanic.first_name
        )
        self.assertEqual(
            response.data[0].get('hours')[1].get('last_name'),
            self.indirect_hours.mechanic.last_name
        )

    def test_query_parameters_are_required(self):
        response = self.client.get(
            reverse('reports:user_hours-list'), content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestReportsByUsersViewSet(APITestCase):

    def test_admin_has_access_to_reports(self):
        admin = AdminFactory()
        self.client.force_login(admin)
        response = self.client.get(
            reverse('reports:users-list'), content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_biller_has_access_to_reports(self):
        biller = BillerFactory()
        self.client.force_login(biller)
        response = self.client.get(
            reverse('reports:users-list'), content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_manager_has_access_to_reports(self):
        manager = ManagerFactory()
        self.client.force_login(manager)
        response = self.client.get(
            reverse('reports:users-list'), content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mechanic_has_access_to_reports(self):
        mechanic = MechanicFactory()
        self.client.force_login(mechanic)
        response = self.client.get(
            reverse('reports:users-list'), content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
