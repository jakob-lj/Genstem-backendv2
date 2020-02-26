
from rest_framework import routers, serializers, viewsets
from rest_framework import exceptions
from rest_framework.renderers import JSONRenderer

from vote.models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name',)

