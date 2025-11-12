from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        return super().create_superuser(email, email, password, **extra_fields)

    def create_user(self, username=None, email=..., password=...,**extrafields):
        return super().create_user(email, email, password, **extrafields)