from django.db import models


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    device_id = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    speed = models.FloatField()
    
    class Meta:
        db_table = 'send_location'