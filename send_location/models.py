from django.db import models

# Create your models here.

class SendLocationModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    id = models.CharField(max_length=50,primary_key=True)
    timestamp = models.TimeField()
    lat = models.CharField(max_length=50)
    lon = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = 'send_location'