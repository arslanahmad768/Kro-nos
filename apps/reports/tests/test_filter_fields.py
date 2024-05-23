from django.test import TestCase

from ..views import ReportsByUsersViewSet, ReportsByServiceTicketsViewSet


class TestReportsByUsersViewSetFilterFields(TestCase):

    def setUp(self):
        self.view = ReportsByUsersViewSet()

    def test_ordering_fields(self):
        ordering_fields = sum(
            self.view.filterset_class.declared_filters.get('ordering').param_map.items(), tuple()
        )
        self.assertTrue('email' in ordering_fields)
        self.assertTrue('first_name' in ordering_fields)
        self.assertTrue('last_name' in ordering_fields)
        self.assertTrue('groups__name' in ordering_fields)
        self.assertTrue('role' in ordering_fields)


class TestReportsByServiceTicketsFilterFields(TestCase):

    def setUp(self):
        self.view = ReportsByServiceTicketsViewSet()

    def test_ordering_fields(self):
        ordering_fields = sum(
            self.view.filterset_class.declared_filters.get('ordering').param_map.items(), tuple()
        )
        self.assertTrue('id' in ordering_fields)
        self.assertTrue('creation_date' in ordering_fields)
        self.assertTrue('date' in ordering_fields)
        self.assertTrue('number' in ordering_fields)
        self.assertTrue('connected_job__number' in ordering_fields)
        self.assertTrue('created_by__first_name' in ordering_fields)
        self.assertTrue('created_by' in ordering_fields)
        self.assertTrue('requester__first_name' in ordering_fields)
        self.assertTrue('requested_by' in ordering_fields)
        self.assertTrue('approval__first_name' in ordering_fields)
        self.assertTrue('approved_by' in ordering_fields)
        self.assertTrue('connected_job__location__name' in ordering_fields)
        self.assertTrue('location' in ordering_fields)
        self.assertTrue('connected_job__customer__name' in ordering_fields)
        self.assertTrue('customer' in ordering_fields)
        self.assertTrue('submitted_for_approval_timestamp' in ordering_fields)
        self.assertTrue('approved_timestamp' in ordering_fields)
