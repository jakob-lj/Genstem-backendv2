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

class Member(models.Model): # used to let members answer to elections in events
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    authenticated = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Election(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    description = models.CharField(default='', max_length=3000)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

class Answer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=200)

class Vote(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    election = models.ForeignKey(Event, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)