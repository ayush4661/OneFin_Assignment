import uuid 
from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    movies = models.JSONField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key = True, 
         default = uuid.uuid4, 
         editable = False
         )
