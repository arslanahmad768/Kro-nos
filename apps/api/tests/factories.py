from datetime import timedelta

from django.utils import timezone

import factory
from factory import fuzzy

from apps.authentication.tests.factories import (
    UserFactory, ManagerFactory, MechanicFactory, BillerFactory
)
from ..models import Attachment, Customer, Location, EmployeeWorkBlock, Job, ServiceTicket


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Location
        django_get_or_create = ('name',)

    name = factory.Faker('currency_code')


class CustomerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Customer

    name = factory.Faker('company')

    @factory.post_generation
    def locations(self, create, extracted, **kwargs):
        if extracted:
            for location in extracted:
                self.locations.add(location)


class JobFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Job
        django_get_or_create = ('number',)

    status = 1
    created_by = factory.SubFactory(BillerFactory)
    description = fuzzy.FuzzyText(prefix='Description ', length=40)
    customer = factory.SubFactory(CustomerFactory)
    location = factory.SubFactory(LocationFactory)
    number = factory.Sequence(lambda n: 'Number {0}'.format(n))

    @factory.post_generation
    def managers(self, create, extracted, **kwargs):
        if extracted:
            for manager in extracted:
                self.managers.add(manager)

    @factory.post_generation
    def mechanics(self, create, extracted, **kwargs):
        if extracted:
            for mechanic in extracted:
                self.mechanics.add(mechanic)
        else:
            mechanics_batch = MechanicFactory.create_batch(3)
            for mechanic in mechanics_batch:
                self.mechanics.add(mechanic)


class AttachmentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Attachment

    description = 'description'
    file = factory.django.FileField(filename='file.png')


class EmployeeWorkBlockFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = EmployeeWorkBlock

    start_time = timezone.now()
    end_time = timezone.now() + timedelta(days=1)
    mileage = 1
    hotel = True
    per_diem = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        service_ticket = kwargs.get('service_ticket')
        if service_ticket is None:
            employee = MechanicFactory()
        else:
            employee = service_ticket.connected_job.mechanics.first()
        kwargs.update({'employee': employee})
        return super()._create(model_class, *args, **kwargs)


class ServiceTicketFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ServiceTicket

    status = 1
    employee_work_block = factory.RelatedFactory(EmployeeWorkBlockFactory, 'service_ticket')
    connected_job = factory.SubFactory(JobFactory)
    created_by = factory.SubFactory(MechanicFactory)
    attachments = factory.RelatedFactory(AttachmentFactory, 'service_ticket')
    date = '2019-2-20'
    unit = 'unit'
    lease_name = 'lease_name'
    county = 'county'
    state = 1
    customer_po_wo = 'customer_po_wo'
    who_called = 'who_called'
    engine_model = 'engine_model'
    engine_serial = 'engine_serial'
    comp_serial = 'comp_serial'
    comp_model = 'comp_model'
    unit_hours = 2
    who_called = 'who_called'
    rpm = 3
    suction = 4
    discharge1 = 5
    discharge2 = 6
    discharge3 = 7
    safety_setting_lo1 = 8
    safety_setting_lo2 = 9
    safety_setting_lo3 = 10
    safety_setting_lo4 = 11
    safety_setting_lo5 = 12
    safety_setting_hi1 = 13
    safety_setting_hi2 = 14
    safety_setting_hi3 = 15
    safety_setting_hi4 = 16
    safety_setting_hi5 = 17
    engine_oil_pressure = 18
    engine_oil_temp = 19
    compressor_oil_pressure = 20
    compressor_oil_temp = 21
    ts1 = 22
    ts2 = 23
    ts3 = 24
    ts4 = 25
    td1 = 26
    td2 = 27
    td3 = 28
    td4 = 29
    cylinder_temperature_hi1 = 30
    cylinder_temperature_hi2 = 31
    cylinder_temperature_hi3 = 32
    cylinder_temperature_hi4 = 33
    exhaust_temperature_l = 34
    exhaust_temperature_r = 35
    exhaust_temperature_hi = 36
    manifold_temperature_l = 37
    manifold_temperature_r = 38
    manifold_temperature_hi = 39
    manifold_pressure_l = 40
    manifold_pressure_r = 41
    manifold_pressure_hi1 = 42
    manifold_pressure_hi2 = 43
    lo_hi = 44
    jacket_water_pressure = 45
    mmcfd = 46
    aux_temp = 47
    hour_meter_reading = 48
    what_was_the_call = 'what_was_the_call'
    what_was_found = 'what_was_found'
    what_was_performed = 'what_was_performed'
    future_work_needed = 'future_work_needed'
    additional_notes = 'additional_notes'
    customer_signature = factory.django.ImageField(filename='picture.png')
    customer_printed_name = 'customer_printed_name'
