from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.conf import settings


class Command(BaseCommand):
    help = 'Create test superuser, use for DEV environment only!'

    def handle(self, **_):
        User = get_user_model()
        if not User.objects.filter(email=settings.DEV_SUPERUSER_EMAIL).exists():
            user = User.objects.create_superuser(
                settings.DEV_SUPERUSER_EMAIL, settings.DEV_SUPERUSER_PASSWORD
            )
            user.groups.add(Group.objects.get(name='Superuser'))
            user.is_confirmed_email = True
        self.stdout.write(self.style.SUCCESS(
            "!!! Pay attention: DEV Superuser '{email}/{pw}' is active !!!".format(
                email=settings.DEV_SUPERUSER_EMAIL, pw=settings.DEV_SUPERUSER_PASSWORD
            )
        ))
