import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Location
from .serializers import LocationSerializers

class LocationApi(APIView):

    def get(self, request):
        device_id = request.GET.get("id")
        lat = request.GET.get("lat")
        lon = request.GET.get("lon")
        speed = request.GET.get("speed")

        data = {
            "device_id": device_id,
            "lat": lat,
            "lon": lon,
            "speed": speed,
            "date_time": datetime.datetime.now()
        }
        serializer =  LocationSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)