from django.db import models
from django.utils import timezone


class Location(models.Model):
    device_id = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    speed = models.FloatField()
    date_time = models.DateTimeField(default=timezone.now)
    