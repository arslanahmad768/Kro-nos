import random
import string
import factory

from ..models import Admin, User, Biller, Manager, Mechanic, Superuser


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    first_name = factory.LazyAttribute(
        lambda a: '{0}{1}'.format(factory.Faker('first_name'),
                                  ''.join(random.choice(string.digits) for i in range(3))))
    last_name = factory.LazyAttribute(
        lambda a: '{0}{1}'.format(factory.Faker('last_name'),
                                  ''.join(random.choice(string.digits) for i in range(3))))
    email = factory.LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name).lower())
    password = factory.PostGenerationMethodCall('set_password', '12345678')


class AdminFactory(UserFactory):

    class Meta:
        model = Admin


class BillerFactory(UserFactory):

    class Meta:
        model = Biller


class ManagerFactory(UserFactory):

    class Meta:
        model = Manager


class MechanicFactory(UserFactory):

    class Meta:
        model = Mechanic


class SuperuserFactory(UserFactory):

    class Meta:
        model = Superuser
