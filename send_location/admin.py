from django.contrib import admin

from .models import Location ,Device


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['device_id','lat','lon','speed','date_time']


@admin.register(Device)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name','unique_id','last_position']
