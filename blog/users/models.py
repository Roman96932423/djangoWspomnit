from django.contrib.auth.models import AbstractUser
from django.db.models import TextField, EmailField

from users.user_manager import UserManager


class User(AbstractUser):
    about_user = TextField(null=True, blank=True, verbose_name="About me")
    email = EmailField(blank=False, db_index=True, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
