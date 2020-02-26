from rest_framework.permissions import IsAuthenticated

from rest_framework import routers, serializers, viewsets
from .serializers import EventSerializer
from .models import Event
from genAuth.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


# ViewSets define the view behavior.
class EventSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return self.queryset.filter(administrators=self.request.user)
