from django.contrib.auth.models import BaseUserManager, Group
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create(self, *args, **kwargs):
        user = self.create_user(*args, **kwargs)
        return user

    def _create_user(self, email, password, **extra_fields):
        """
        Creates, saves a user with passed email and password.
        """
        if not email:
            raise ValueError(_('Email is required and must be set.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)


class ProxyUserManager(BaseUserManager):
    """
    Abstract manager class for proxy models.
    """

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        group = Group.objects.get(name=user.__class__.__name__)
        user.groups.add(group)
        return user


class AdminUserManager(ProxyUserManager):
    """
    Custom manager class for Admin proxy model.
    """

    def get_queryset(self):
        return super().get_queryset().filter(groups__name='Admin')


class BillerUserManager(ProxyUserManager):
    """
    Custom manager class for Biller proxy model.
    """

    def get_queryset(self):
        return super().get_queryset().filter(groups__name='Biller')


class ManagerUserManager(ProxyUserManager):
    """
    Custom manager class for Manager proxy model.
    """

    def get_queryset(self):
        return super().get_queryset().filter(groups__name='Manager')


class MechanicUserManager(ProxyUserManager):
    """
    Custom manager class for Mechanic proxy model.
    """

    def get_queryset(self):
        return super().get_queryset().filter(groups__name='Mechanic')


class SuperuserManager(ProxyUserManager):
    """
    Custom manager class for Superuser proxy model.
    """

    def get_queryset(self):
        return super().get_queryset().filter(groups__name='Superuser')
