
from rest_framework import routers, serializers, viewsets
from rest_framework import exceptions
from rest_framework.renderers import JSONRenderer

from vote.models import Event, Election

class ElectionSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Election
        fields = ('id', 'active', 'description')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    election_set = ElectionSerializer(many=True)
    class Meta:
        model = Event
        fields = ('name', 'active', 'startDate', 'election_set',)

