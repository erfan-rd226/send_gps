from rest_framework.views import APIView
from rest_framework.response import Response
from send_location.models import Location
from rest_framework import serializers

from send_location.services import create_location_device
from send_location.types.location_type import LocationInterface



class LocationApi(APIView):

    class InputSerializer(serializers.Serializer):
        device_id = serializers.CharField()
        lat = serializers.CharField()
        lon = serializers.CharField()
        speed = serializers.CharField()

    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Location
            fields = "__all__"


    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        location_data = LocationInterface(
            device_id=serializer.validated_data.get("device_id"),
            lat=serializer.validated_data.get("lat"),
            lon=serializer.validated_data.get("lon"),
            speed=serializer.validated_data.get("speed"),
        )
        location_data = create_location_device(location_data=location_data)

        return Response(self.OutPutSerializer(location_data).data, status=201)
