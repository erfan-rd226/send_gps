from django.shortcuts import render

from rest_framework import generics

from . import models 
from . import serializers 

# Create your views here.

class SendLocationViewSet(generics.ListCreateAPIView):
    queryset = models.SendLocationModel.objects.all()
    serializer_class = serializers.SendLocationSerializers