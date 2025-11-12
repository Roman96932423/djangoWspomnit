from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import TextField, EmailField


class User(AbstractUser):
    about_user = TextField(null=True, blank=True, verbose_name="About me")
    email = EmailField(blank=False, db_index=True, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
