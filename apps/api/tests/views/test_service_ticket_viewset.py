import json

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase

from apps.authentication.tests.factories import (
    MechanicFactory, AdminFactory, ManagerFactory
)
from ..factories import (
    AttachmentFactory, EmployeeWorkBlockFactory, JobFactory, ServiceTicketFactory
    )
from ...utils import delete_file
from ...models import Attachment, EmployeeWorkBlock, ServiceTicket
from apps.notifications.models import Action


class TestServiceTicketViewSet(APITestCase):

    def setUp(self):
        self.mechanic = MechanicFactory()
        self.manager = ManagerFactory()
        self.connected_job = JobFactory(mechanics=(self.mechanic,), managers=(self.manager,))
        self.st = ServiceTicketFactory(connected_job=self.connected_job)
        self.attachment = AttachmentFactory(service_ticket=self.st)
        self.client.force_login(self.mechanic)
        self.file = SimpleUploadedFile(
            'file.jpg', bytes('some bytes', encoding='UTF-8'), content_type='image/jpg'
        )
        self.st_data = {
            'status': 1,
            'connected_job': self.connected_job.id,
            'employee_works[0]employee': self.mechanic.id,
            'employee_works[0]start_time': '02/20/2019 7:45 AM',
            'employee_works[0]end_time': '02/20/2019 5:30 PM',
            'employee_works[0]mileage': '1.0',
            'employee_works[0]hotel': False,
            'employee_works[0]per_diem': True,
            'created_by': self.mechanic.id,
            'attachments[0]file': self.file,
            'attachments[0]description': self.attachment.description,
            'date': '2-20-2019',
            'unit': 'Unit',
            'lease_name': 'Lease Name',
            'county': 'County',
            'state': 18,
            'customer_po_wo': 'customer_po_wo',
            'who_called': 'who_called',
            'engine_model': 'engine_model',
            'engine_serial': 'engine_serial',
            'comp_model': 'Comp Model',
            'comp_serial': 'Comp Serial',
            'unit_hours': 1,
            'rpm': '0.1',
            'suction': '0.3',
            'discharge1': '0.1',
            'discharge2': '1.0',
            'discharge3': '2.0',
            'safety_setting_lo1': '3.0',
            'safety_setting_lo2': '4.0',
            'safety_setting_lo3': '5.0',
            'safety_setting_lo4': '6.0',
            'safety_setting_lo5': '7.0',
            'safety_setting_hi1': '8.0',
            'safety_setting_hi2': '9.0',
            'safety_setting_hi3': '8.0',
            'safety_setting_hi4': '7.0',
            'safety_setting_hi5': '6.0',
            'engine_oil_pressure': '5.0',
            'engine_oil_temp': '4.0',
            'compressor_oil_pressure': '3.0',
            'compressor_oil_temp': '2.0',
            'ts1': '1.0',
            'ts2': '2.0',
            'ts3': '3.0',
            'ts4': '4.0',
            'td1': '5.0',
            'td2': '6.0',
            'td3': '7.0',
            'td4': '8.0',
            'cylinder_temperature_hi1': '9.0',
            'cylinder_temperature_hi2': '8.0',
            'cylinder_temperature_hi3': '7.0',
            'cylinder_temperature_hi4': '6.0',
            'exhaust_temperature_l': '5.0',
            'exhaust_temperature_r': '4.0',
            'exhaust_temperature_hi': '3.0',
            'manifold_temperature_l': '2.0',
            'manifold_temperature_r': '1.0',
            'manifold_temperature_hi': '2.0',
            'manifold_pressure_l': '3.0',
            'manifold_pressure_r': '2.0',
            'manifold_pressure_hi1': '1.0',
            'manifold_pressure_hi2': '2.0',
            'lo_hi': '3.0',
            'jacket_water_pressure': '2.0',
            'mmcfd': '1.0',
            'aux_temp': '2.0',
            'hour_meter_reading': '3.0',
            'what_was_the_call': 'asd',
            'what_was_found': 'dsa',
            'what_was_performed': 'what_was_performed',
            'future_work_needed': 'future_work_needed',
            'additional_notes': 'additional_notes',
            'customer_printed_name': 'customer_printed_name'
        }

    def tearDown(self):
        delete_file(self.st.customer_signature.path)
        for attachment in Attachment.objects.all():
            delete_file(attachment.file.path)

    def test_create_service_ticket(self):

        url = reverse('api:service_ticket-list')
        response = self.client.post(
            url,
            data=self.st_data,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data.get('created_by').get('id'), self.st_data.get('created_by')
        )
        self.assertEqual(response.data.get('created_by').get('id'), self.st_data.get('created_by'))
        self.assertEqual(
            response.data.get('connected_job').get('id'), self.st_data.get('connected_job')
        )
        self.assertEqual(response.data.get('unit'), self.st_data.get('unit'))
        self.assertEqual(response.data.get('lease_name'), self.st_data.get('lease_name'))
        self.assertEqual(response.data.get('county'), self.st_data.get('county'))
        self.assertEqual(response.data.get('state').get('value'), self.st_data.get('state'))
        self.assertEqual(response.data.get('customer_po_wo'), self.st_data.get('customer_po_wo'))
        self.assertEqual(response.data.get('who_called'), self.st_data.get('who_called'))
        self.assertEqual(response.data.get('engine_model'), self.st_data.get('engine_model'))
        self.assertEqual(response.data.get('engine_serial'), self.st_data.get('engine_serial'))
        self.assertEqual(response.data.get('comp_model'), self.st_data.get('comp_model'))
        self.assertEqual(response.data.get('comp_serial'), self.st_data.get('comp_serial'))
        self.assertEqual(response.data.get('unit_hours'), self.st_data.get('unit_hours'))
        self.assertEqual(response.data.get('rpm'), self.st_data.get('rpm'))
        self.assertEqual(response.data.get('suction'), self.st_data.get('suction'))
        self.assertEqual(response.data.get('discharge1'), self.st_data.get('discharge1'))
        self.assertEqual(response.data.get('discharge2'), self.st_data.get('discharge2'))
        self.assertEqual(response.data.get('discharge3'), self.st_data.get('discharge3'))
        self.assertEqual(
            response.data.get('safety_setting_lo1'), self.st_data.get('safety_setting_lo1'))
        self.assertEqual(
            response.data.get('safety_setting_lo2'), self.st_data.get('safety_setting_lo2'))
        self.assertEqual(
            response.data.get('safety_setting_lo3'), self.st_data.get('safety_setting_lo3'))
        self.assertEqual(
            response.data.get('safety_setting_lo4'), self.st_data.get('safety_setting_lo4'))
        self.assertEqual(
            response.data.get('safety_setting_lo5'), self.st_data.get('safety_setting_lo5'))
        self.assertEqual(
            response.data.get('safety_setting_hi1'), self.st_data.get('safety_setting_hi1'))
        self.assertEqual(
            response.data.get('safety_setting_hi2'), self.st_data.get('safety_setting_hi2'))
        self.assertEqual(
            response.data.get('safety_setting_hi3'), self.st_data.get('safety_setting_hi3'))
        self.assertEqual(
            response.data.get('safety_setting_hi4'), self.st_data.get('safety_setting_hi4'))
        self.assertEqual(
            response.data.get('safety_setting_hi5'), self.st_data.get('safety_setting_hi5'))
        self.assertEqual(
            response.data.get('engine_oil_pressure'), self.st_data.get('engine_oil_pressure'))
        self.assertEqual(response.data.get('engine_oil_temp'), self.st_data.get('engine_oil_temp'))
        self.assertEqual(
            response.data.get('compressor_oil_pressure'),
            self.st_data.get('compressor_oil_pressure')
        )
        self.assertEqual(
            response.data.get('compressor_oil_temp'), self.st_data.get('compressor_oil_temp'))
        self.assertEqual(response.data.get('ts1'), self.st_data.get('ts1'))
        self.assertEqual(response.data.get('ts2'), self.st_data.get('ts2'))
        self.assertEqual(response.data.get('ts3'), self.st_data.get('ts3'))
        self.assertEqual(response.data.get('ts4'), self.st_data.get('ts4'))
        self.assertEqual(response.data.get('td1'), self.st_data.get('td1'))
        self.assertEqual(response.data.get('td2'), self.st_data.get('td2'))
        self.assertEqual(response.data.get('td3'), self.st_data.get('td3'))
        self.assertEqual(response.data.get('td4'), self.st_data.get('td4'))
        self.assertEqual(
            response.data.get('cylinder_temperature_hi1'),
            self.st_data.get('cylinder_temperature_hi1')
        )
        self.assertEqual(
            response.data.get('cylinder_temperature_hi2'),
            self.st_data.get('cylinder_temperature_hi2')
        )
        self.assertEqual(
            response.data.get('cylinder_temperature_hi1'),
            self.st_data.get('cylinder_temperature_hi1')
        )
        self.assertEqual(
            response.data.get('cylinder_temperature_hi3'),
            self.st_data.get('cylinder_temperature_hi3')
        )
        self.assertEqual(
            response.data.get('exhaust_temperature_l'), self.st_data.get('exhaust_temperature_l')
        )
        self.assertEqual(
            response.data.get('exhaust_temperature_r'), self.st_data.get('exhaust_temperature_r')
        )
        self.assertEqual(
            response.data.get('exhaust_temperature_hi'), self.st_data.get('exhaust_temperature_hi')
        )
        self.assertEqual(
            response.data.get('manifold_temperature_l'), self.st_data.get('manifold_temperature_l')
        )
        self.assertEqual(
            response.data.get('manifold_temperature_r'), self.st_data.get('manifold_temperature_r')
        )
        self.assertEqual(
            response.data.get('manifold_temperature_hi'),
            self.st_data.get('manifold_temperature_hi')
        )
        self.assertEqual(
            response.data.get('manifold_pressure_l'), self.st_data.get('manifold_pressure_l')
        )
        self.assertEqual(
            response.data.get('manifold_pressure_r'), self.st_data.get('manifold_pressure_r')
        )
        self.assertEqual(
            response.data.get('manifold_pressure_hi1'), self.st_data.get('manifold_pressure_hi1')
        )
        self.assertEqual(
            response.data.get('manifold_pressure_hi2'), self.st_data.get('manifold_pressure_hi2')
        )
        self.assertEqual(response.data.get('lo_hi'), self.st_data.get('lo_hi'))
        self.assertEqual(
            response.data.get('jacket_water_pressure'), self.st_data.get('jacket_water_pressure')
        )
        self.assertEqual(response.data.get('mmcfd'), self.st_data.get('mmcfd'))
        self.assertEqual(response.data.get('aux_temp'), self.st_data.get('aux_temp'))
        self.assertEqual(
            response.data.get('hour_meter_reading'), self.st_data.get('hour_meter_reading')
        )
        self.assertEqual(
            response.data.get('what_was_the_call'), self.st_data.get('what_was_the_call')
        )
        self.assertEqual(response.data.get('what_was_found'), self.st_data.get('what_was_found'))
        self.assertEqual(
            response.data.get('what_was_performed'), self.st_data.get('what_was_performed')
        )
        self.assertEqual(
            response.data.get('future_work_needed'), self.st_data.get('future_work_needed')
        )
        self.assertEqual(
            response.data.get('additional_notes'), self.st_data.get('additional_notes')
        )
        self.assertEqual(
            response.data.get('customer_signature'), self.st_data.get('customer_signature')
        )
        self.assertEqual(
            response.data.get('customer_printed_name'), self.st_data.get('customer_printed_name')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('start_time'),
            self.st_data.get('employee_works[0]start_time')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('end_time'),
            self.st_data.get('employee_works[0]end_time')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('mileage'),
            self.st_data.get('employee_works[0]mileage')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('hotel'),
            self.st_data.get('employee_works[0]hotel')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('per_diem'),
            self.st_data.get('employee_works[0]per_diem')
        )

    def test_archived_st(self):
        self.client.force_login(AdminFactory())
        error_id = 10000000
        self.assertFalse(self.st.is_archive)
        all_action = Action.objects.filter(connected_object_id=self.st.id)
        for i in all_action:
            self.assertFalse(i.is_viewed)
        restore_data = {'ids': [self.st.id, error_id]}
        url = reverse('api:service_ticket-archive-service-ticket')
        response = self.client.post(
            url,
            data=json.dumps(restore_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('Successfully archived Service Ticket (IDs)'),
            [self.st.id]
        )
        self.assertEqual(
            response.data.get('Failed to archive Service Ticket (IDs)'),
            [error_id]
        )
        new_st = ServiceTicket.objects.get(id=self.st.id).is_archive
        all_action = Action.objects.filter(connected_object_id=self.st.id)
        for i in all_action:
            self.assertTrue(i.is_viewed)
        self.assertTrue(new_st)

    def test_archived_st_with_wrong_role(self):
        new_user = ManagerFactory()
        self.client.force_login(new_user)
        id = self.st.id
        url = reverse('api:service_ticket-archive-service-ticket')
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

    def test_delete_attachments(self):
        attachment = Attachment.objects.get_or_create(id=1, service_ticket=self.st)[0]
        attachment.file = self.file
        attachment.save()
        url = reverse('api:service_ticket-delete-attachments', args=[self.st.id])
        response = self.client.patch(
            url,
            data=json.dumps({'attachment_ids': [attachment.id]}),
            content_type='application/json'
        )
        self.st.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('attachments')), self.st.attachments.count())
        self.assertNotIn(attachment, self.st.attachments.all())

    def test_clean_employee(self):
        self.new_st_data = {
            'status': 1,
            'connected_job': self.connected_job.id,
            'employee_works[0]employee': MechanicFactory().id,
            'employee_works[0]start_time': '02/20/2019 7:45 AM',
            'employee_works[0]end_time': '02/20/2019 5:30 PM',
            'employee_works[0]mileage': '1.0',
            'employee_works[0]hotel': False,
            'employee_works[0]per_diem': True,
            'created_by': self.mechanic.id,
        }
        url = reverse('api:service_ticket-list')
        response = self.client.post(
            url,
            data=self.new_st_data,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get('employee')[0],
            'Selected employee is not present in the related Job.'
        )

    def test_update_service_ticket(self):
        new_mechanic = MechanicFactory()
        self.st.connected_job.mechanics.add(new_mechanic)
        data = {
            'status': 2,
            'employee_works[0]id': self.st.employee_works.first().id,
            'employee_works[0]start_time': '02/20/2019 7:45 AM',
            'employee_works[0]end_time': '02/20/2019 5:30 PM',
            'employee_works[0]mileage': '1.5',
            'employee_works[0]hotel': True,
            'employee_works[0]per_diem': False,
            'employee_works[0]employee': new_mechanic.id
        }

        url = reverse('api:service_ticket-detail', args=[self.st.id])
        response = self.client.patch(
            url,
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status').get('value'), data.get('status'))
        self.assertEqual(
            response.data.get('employee_works')[0].get('id'),
            data.get('employee_works[0]id')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('start_time'),
            data.get('employee_works[0]start_time')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('end_time'),
            data.get('employee_works[0]end_time')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('mileage'),
            data.get('employee_works[0]mileage')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('hotel'),
            data.get('employee_works[0]hotel')
        )

    def test_time_validation(self):
        self.st_data.update({
            'employee_works[0]employee': self.connected_job.mechanics.last().id,
            'employee_works[0]start_time': '02/20/2019 5:30 PM',
            'employee_works[0]end_time': '02/20/2019 7:45 AM',
            'employee_works[0]mileage': '1.0',
            'employee_works[0]hotel': False,
            'employee_works[0]per_diem': True
        })

        url = reverse('api:service_ticket-list')
        response = self.client.post(
            url,
            data=self.st_data,
        )

        result = response.data.get('employee_works', [{}])[0].get('start_time', [])[0]
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result, 'Start Time can not be ahead of the End Time')

    def test_time_update_validation(self):
        url = reverse('api:service_ticket-detail', args=[self.st.id])
        data = {
            'employee_works[0]start_time': '02/20/2019 5:30 PM',
            'employee_works[0]end_time': '02/20/2019 7:45 AM'
        }
        response = self.client.patch(url, data=data)

        result = response.data.get('employee_works', [{}])[0].get('start_time', [])[0]
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result, 'Start Time can not be ahead of the End Time')

    def test_delete_employee_works(self):
        employee_work = EmployeeWorkBlock.objects.create(
            service_ticket=self.st, employee_id=self.mechanic.id
        )
        url = reverse('api:service_ticket-delete-employee-works', args=[self.st.id])
        response = self.client.patch(
            url,
            data=json.dumps({'employee_work_ids': [employee_work.id]}),
            content_type='application/json'
        )
        self.st.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('employee_works')), self.st.employee_works.count())
        self.assertNotIn(employee_work, self.st.employee_works.all())

    def test_add_employee_to_service_ticket(self):
        new_mechanic = MechanicFactory()
        self.st.connected_job.mechanics.add(new_mechanic)
        data = {
            'employee_works[0]id': self.st.employee_works.first().id,
            'employee_works[0]start_time': '02/20/2019 7:45 AM',
            'employee_works[0]end_time': '02/20/2019 5:30 PM',
            'employee_works[0]mileage': '1.5',
            'employee_works[0]hotel': True,
            'employee_works[0]per_diem': False,
            'employee_works[0]employee': new_mechanic.id,
            'employee_works[1]mileage': '2.5',
            'employee_works[1]start_time': '02/20/2019 7:45 AM',
            'employee_works[1]end_time': '02/20/2019 5:30 PM',
            'employee_works[1]hotel': False,
            'employee_works[1]per_diem': True,
            'employee_works[1]employee': new_mechanic.id
        }

        url = reverse('api:service_ticket-detail', args=[self.st.id])
        response = self.client.patch(
            url,
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('employee_works')[0].get('id'),
            data.get('employee_works[0]id')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('start_time'),
            data.get('employee_works[0]start_time')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('end_time'),
            data.get('employee_works[0]end_time')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('mileage'),
            data.get('employee_works[0]mileage')
        )
        self.assertEqual(
            response.data.get('employee_works')[0].get('hotel'),
            data.get('employee_works[0]hotel')
        )
        self.assertIn('id', response.data.get('employee_works')[1])
        self.assertEqual(
            response.data.get('employee_works')[1].get('start_time'),
            data.get('employee_works[1]start_time')
        )
        self.assertEqual(
            response.data.get('employee_works')[1].get('end_time'),
            data.get('employee_works[1]end_time')
        )
        self.assertEqual(
            response.data.get('employee_works')[1].get('mileage'),
            data.get('employee_works[1]mileage')
        )
        self.assertEqual(
            response.data.get('employee_works')[1].get('hotel'),
            data.get('employee_works[1]hotel')
        )

    def test_update_service_ticket_in_status_pending_for_approval(self):
        st = ServiceTicketFactory(
            requester=self.mechanic,
            status=ServiceTicket.PENDING_FOR_APPROVAL,
            connected_job=self.connected_job
        )
        data = {
            'employee_works[0]id': st.employee_works.first().id,
            'employee_works[0]start_time': '02/20/2019 7:45 AM',
            'employee_works[0]end_time': '02/20/2019 5:30 PM',
            'employee_works[0]mileage': '1.0',
            'employee_works[0]hotel': False,
            'employee_works[0]per_diem': True,
            'employee_works[0]employee': self.mechanic.id
        }

        url = reverse('api:service_ticket-detail', args=[st.id])
        response = self.client.patch(
            url,
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_required_fields(self):
        new_st = ServiceTicketFactory(
            unit='',
            date=None,
            connected_job=self.connected_job
        )
        url = reverse('api:service_ticket-detail', args=[new_st.id])
        st_data = {
            'status': 2,
        }
        response = self.client.patch(
            url,
            data=st_data,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get('date')[0],
            'Date is required.'
        )

    def test_update_Attachment_file(self):
        url = reverse('api:service_ticket-detail', args=[self.st.id])
        data = {
            'attachments[0]id': self.st.attachments.first().id,
            'attachments[0]description': self.attachment.description,
            'attachments[0]file': 'This should be ignored'
        }
        response = self.client.patch(
            url,
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_Attachment_without_file(self):
        url = reverse('api:service_ticket-detail', args=[self.st.id])
        data = {
            'attachments[0]description': self.attachment.description
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_ST_without_employee(self):
        url = reverse('api:service_ticket-detail', args=[self.st.id])
        data = {
            'employee_works[0]start_time': '02/20/2019 5:45 AM'
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get('employee'),
            'Employee is required for creating Service Ticket.'
        )

    def test_delete_all_employee_works(self):
        self.assertGreater(self.st.employee_works.count(), 0)
        url = reverse('api:service_ticket-detail', args=[self.st.id])
        data = {
            'employee_works': ''
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.st.refresh_from_db()
        self.assertEqual(self.st.employee_works.count(), 0)

    def test_delete_all_attachments(self):
        self.assertGreater(self.st.attachments.count(), 0)
        url = reverse('api:service_ticket-detail', args=[self.st.id])
        data = {
            'attachments': ''
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.st.refresh_from_db()
        self.assertEqual(self.st.attachments.count(), 0)

    def test_update_customer_signature_if_exists(self):
        url = reverse('api:service_ticket-detail', args=[self.st.id])
        data = {
            'customer_signature': 'This should be ignored',
            'lease_name': 'Just update other field'
        }
        response = self.client.patch(
            url,
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
