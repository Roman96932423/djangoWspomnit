from django.conf import settings
from django.db.models import (
    Model, 
    CharField, 
    TextField, 
    DateTimeField, 
    ForeignKey,
    CASCADE
    )


class Post(Model):
    title = CharField(max_length=100, null=False, blank=False)
    content = TextField(null=False, blank=False)
    created_at = DateTimeField(auto_now_add=True)
    created_by = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created_at']
