from django.contrib.auth.models import AbstractUser
from django.db.models import TextField, EmailField
from django_resized import ResizedImageField

from users.user_manager import UserManager
from utils.photo_path import get_photo_path


class User(AbstractUser):
    about_user = TextField(null=True, blank=True, verbose_name="About me")
    email = EmailField(blank=False, db_index=True, unique=True)
    user_image = ResizedImageField(
        null=True, blank=True,
        size=[300, 300],
        quality=100,
        upload_to=get_photo_path
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
