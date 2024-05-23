from django.test import TestCase

from .factories import AdminFactory, UserFactory, BillerFactory, ManagerFactory, MechanicFactory


class TestUserModel(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), self.user.first_name)

    def test_get_full_name(self):
        self.assertEqual(
            '{0} {1}'.format(self.user.first_name, self.user.last_name),
            self.user.get_full_name()
        )

    def test_str_method(self):
        self.assertEqual(str(self.user), self.user.get_full_name())

    def test_is_admin(self):
        user = AdminFactory()
        self.assertTrue(user.is_admin)

    def test_is_biller(self):
        user = BillerFactory()
        self.assertTrue(user.is_biller)

    def test_is_manager(self):
        user = ManagerFactory()
        self.assertTrue(user.is_manager)

    def test_is_mechanic(self):
        user = MechanicFactory()
        self.assertTrue(user.is_mechanic)


class TestAdminModel(TestCase):

    def setUp(self):
        self.admin = AdminFactory()

    def test_save_method(self):
        new_admin = AdminFactory()
        self.assertTrue(new_admin.is_superuser)
