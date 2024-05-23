from django.test import TestCase

from ...views import JobViewSet, ServiceTicketViewSet


class TestServiceTicketFilterFields(TestCase):

    def setUp(self):
        self.st = ServiceTicketViewSet()

    def test_search_fields(self):
        self.assertTrue('connected_job__location__name' in self.st.search_fields)
        self.assertTrue('connected_job__customer__name' in self.st.search_fields)
        self.assertTrue('connected_job__number' in self.st.search_fields)
        self.assertTrue('additional_notes' in self.st.search_fields)
        self.assertTrue('created_by__first_name' in self.st.search_fields)
        self.assertTrue('created_by__last_name' in self.st.search_fields)

    def test_filter_fields(self):
        self.assertTrue('status' in self.st.filterset_class.declared_filters)
        self.assertTrue('start_date' in self.st.filterset_class.declared_filters)
        self.assertTrue('end_date' in self.st.filterset_class.declared_filters)
        self.assertTrue('job_number' in self.st.filterset_class.declared_filters)

    def test_ordering_fields(self):
        ordering_fields = sum(
            self.st.filterset_class.declared_filters.get('ordering').param_map.items(), tuple()
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
        self.assertTrue('additional_notes' in ordering_fields)
        self.assertTrue('notes' in ordering_fields)


class TestJobFilterFields(TestCase):

    def setUp(self):
        self.job = JobViewSet()

    def test_search_fields(self):
        self.assertTrue('location__name' in self.job.search_fields)
        self.assertTrue('customer__name' in self.job.search_fields)
        self.assertTrue('number' in self.job.search_fields)
        self.assertTrue('created_by__first_name' in self.job.search_fields)
        self.assertTrue('created_by__last_name' in self.job.search_fields)

    def test_filter_fields(self):
        self.assertTrue('status' in self.job.filterset_class.declared_filters)
        self.assertTrue('start_date' in self.job.filterset_class.declared_filters)
        self.assertTrue('end_date' in self.job.filterset_class.declared_filters)
        self.assertTrue('all_tickets_approved' in self.job.filterset_class.declared_filters)

    def test_ordering_fields(self):
        ordering_fields = sum(
            self.job.filterset_class.declared_filters.get('ordering').param_map.items(), tuple()
        )
        self.assertTrue('number' in ordering_fields)
        self.assertTrue('status' in ordering_fields)
        self.assertTrue('created_by__first_name' in ordering_fields)
        self.assertTrue('created_by' in ordering_fields)
        self.assertTrue('requester__first_name' in ordering_fields)
        self.assertTrue('requested_by' in ordering_fields)
        self.assertTrue('approval__first_name' in ordering_fields)
        self.assertTrue('approved_by' in ordering_fields)
        self.assertTrue('location__name' in ordering_fields)
        self.assertTrue('location' in ordering_fields)
        self.assertTrue('customer__name' in ordering_fields)
        self.assertTrue('customer' in ordering_fields)
        self.assertTrue('creation_date' in ordering_fields)
        self.assertTrue('time_stamp' in ordering_fields)
