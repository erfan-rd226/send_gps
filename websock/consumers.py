from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import json
from asgiref.sync import sync_to_async
from send_location.models import Device, Location
from django.db import connection


class SendLocationConsumer(AsyncWebsocketConsumer):
     async def connect(self):
          await self.accept()
          await self.send(text_data=f"hello")
          self.task = asyncio.create_task(self.send_data())
          return super().connect()
    
     async def disconnect(self, code):
          if hasattr(self, "task"):
               self.task.cancel()
          return await super().disconnect(code)
     
     async def receive(self, text_data=None):
          await self.send(text_data=text_data)
          # devices = await sync_to_async(list)(Device.objects.all())
          # locations = await sync_to_async(list)(Location.objects.all())
          # while True:
          #      for location_item, device_item in zip(locations, devices):
          #           if location_item.id == device_item.last_position_id :
          #                data = {
          #                     "id":location_item.id, 
          #                     "lat": location_item.lat, 
          #                     "lon":location_item.lon, 
          #                     "date_time": str(location_item.date_time), 
          #                     "device": location_item.device_id
          #                }
          #                await self.send(text_data=str(data))
          #      await asyncio.sleep(3)

     async def send_data(self):
          while True:
               devices = await sync_to_async(list)(Device.objects.all())
               locations = await sync_to_async(list)(Location.objects.all())
               for location_item in locations:
                    for device_item in devices:
                         if location_item.id == device_item.last_position_id :
                              print(location_item.id, device_item.last_position_id)
                              data = {
                                   "id":location_item.id, 
                                   "lat": location_item.lat, 
                                   "lon":location_item.lon, 
                                   "date_time": str(location_item.date_time), 
                                   "device": location_item.device_id
                              }
                              await self.send(text_data=str(data))
                              await asyncio.sleep(0.1)
               await asyncio.sleep(4)
