from django.db import models
import uuid

from genAuth.models import User

# Create your models here.
class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    administrators = models.ManyToManyField(User)
    name = models.CharField(default='', max_length=200)
    startDate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)