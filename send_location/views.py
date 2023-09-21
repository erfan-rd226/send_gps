from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    id = request.GET.get("id")
    device_id = request.GET.get("device_id")
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    speed = request.GET.get("speed")

    print(request.GET)

    return HttpResponse("ok")