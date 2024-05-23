from django.test import TestCase

from ..views import IndirectHoursViewSet


class TestIndirectHoursSearchFields(TestCase):

    def setUp(self):
        self.indirect = IndirectHoursViewSet()

    def test_search_fields(self):
        self.assertTrue('mechanic__first_name' in self.indirect.search_fields)
        self.assertTrue('mechanic__last_name' in self.indirect.search_fields)


class TestIndirectHoursFilterFields(TestCase):

    def setUp(self):
        self.indirect = IndirectHoursViewSet()

    def test_filter_fields(self):
        self.assertTrue('status' in self.indirect.filterset_class.declared_filters)
        self.assertTrue('start_date' in self.indirect.filterset_class.declared_filters)
        self.assertTrue('end_date' in self.indirect.filterset_class.declared_filters)
        self.assertTrue('is_archive' in self.indirect.filterset_class.declared_filters)

    def test_ordering_fields(self):
        ordering_fields = sum(
            self.indirect.filterset_class.declared_filters.get('ordering').param_map.items(),
            tuple()
        )
        self.assertTrue('date' in ordering_fields)
        self.assertTrue('mechanic__first_name' in ordering_fields)
        self.assertTrue('mechanic' in ordering_fields)
        self.assertTrue('hours' in ordering_fields)
        self.assertTrue('time_code' in ordering_fields)
        self.assertTrue('status' in ordering_fields)
        self.assertTrue('notes' in ordering_fields)
