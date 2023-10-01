from .models import Location , Device
from rest_framework import serializers


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "device_id", "lat", "lon", "speed", "date_time"]
    
    def create(self, validated_data):
        location = Location.objects.create(
            device_id=validated_data["device_id"],
            lat = validated_data["lat"],
            lon = validated_data["lon"],
            speed = validated_data["speed"]
        )
        device = Device.objects.get(unique_id=int(validated_data["device_id"]))
        device.last_position = location
        device.save()
        return location

class DeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['last_position']