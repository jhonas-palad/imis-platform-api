from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import ServiceSerializer
from .models import Service

class ServiceView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


    