from django.conf import settings
from django.db.models import (
    Model, 
    CharField, 
    TextField, 
    DateTimeField, 
    ForeignKey,
    CASCADE
    )
from django_resized import ResizedImageField

from utils.photo_path import get_photo_path


class Post(Model):
    title = CharField(max_length=100, null=False, blank=False)
    teaser = CharField(max_length=100, null=True, blank=True)
    content = TextField(null=False, blank=False)
    created_at = DateTimeField(auto_now_add=True)
    created_by = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    header_image = ResizedImageField(
        null=True, blank=True,
        size=[700, 220],
        quality=100,
        upload_to = get_photo_path
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created_at']
