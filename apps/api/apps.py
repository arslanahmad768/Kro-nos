from django.apps import AppConfig
from django.db.models.signals import post_save

# from .signals import service_ticket_changed


class ApiConfig(AppConfig):
    name = 'apps.api'

    def ready(self):
        import apps.api.signals
        import apps.time_tracker.signals