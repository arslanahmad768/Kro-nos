from django.test import TestCase

from ..views import UserViewSet


class TestUserSearchFields(TestCase):

    def setUp(self):
        self.user = UserViewSet()

    def test_search_fields(self):
        self.assertTrue('first_name' in self.user.search_fields)
        self.assertTrue('last_name' in self.user.search_fields)
        self.assertTrue('groups__name' in self.user.search_fields)
        self.assertTrue('email' in self.user.search_fields)


class TestUserFilterFields(TestCase):

    def setUp(self):
        self.user = UserViewSet()

    def test_filter_fields(self):
        self.assertTrue('role' in self.user.filterset_class.declared_filters)
        self.assertTrue('status' in self.user.filterset_class.declared_filters)

    def test_ordering_fields(self):
        ordering_fields = sum(
            self.user.filterset_class.declared_filters.get('ordering').param_map.items(), tuple()
        )
        self.assertTrue('first_name' in ordering_fields)
        self.assertTrue('name' in ordering_fields)
        self.assertTrue('groups__name' in ordering_fields)
        self.assertTrue('role' in ordering_fields)
        self.assertTrue('email' in ordering_fields)
