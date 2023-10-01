from django.db import models
from django.utils import timezone


class Location(models.Model):
    device_id = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    speed = models.FloatField()
    date_time = models.DateTimeField(default=timezone.now)


class Device(models.Model):
    name = models.TextField(max_length=50)
    unique_id = models.IntegerField(unique=True)
    last_position = models.ForeignKey('Location', related_name='last_position', on_delete=models.CASCADE, null=True)
    lat = models.ForeignKey('Location', related_name='lats', on_delete=models.CASCADE, null=True)
    lon = models.ForeignKey('Location', related_name='lons', on_delete=models.CASCADE, null=True)
    updated_time = models.DateTimeField(auto_now_add=True)