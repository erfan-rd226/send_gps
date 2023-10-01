import datetime
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from send_location.models import Device, Location
from django.views.decorators.csrf import csrf_exempt
from .serializers import LocationSerializers, DeviceSerializers

class LocationApi(APIView):

    def post(self, request):
        serializer = LocationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=400)

        


# class DeviceApi(APIView):

#     def get(self,request):
#         device = Device.objects.all()
#         serializer = DeviceSerializers(device)
#         serializer.save()