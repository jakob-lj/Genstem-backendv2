from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os

# Create your views here.
class EnvironmentView(APIView):
    def get(self, request):
        """
        Get environemnt variables
        """
        domain = os.environ.get('DOMAIN')
        if domain:
            return Response({'domain':domain})
        else:
            return Response({'domain':'unknown domain'})

class StatusView(APIView):
    def get(self, request):
        """
        just a simple view to ping the backend
        """
        return Response(status=200)