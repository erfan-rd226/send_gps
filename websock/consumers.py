from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import json
from asgiref.sync import sync_to_async
from send_location.models import Location

class SendLocationConsumer(AsyncWebsocketConsumer):
     async def connect(self):
          await self.accept()
          await self.send(text_data=f"")
          return super().connect()
    
     async def disconnect(self, code):
          return await super().disconnect(code)
    
     async def receive(self, text_data=None):
          locations = await sync_to_async(list)(Location.objects.all())
          counter = 0
          while True:
               location = locations[counter]
               data = {"lat": location.lat, "lon":location.lon, "date_time": str(location.date_time), "device": location.device_id}
               await self.send(text_data=str(data))
               counter += 1
               await asyncio.sleep(3)

     
     async def update_last_saved_data(self, event):
          data = locals.objects.last()
          await self.send(data)
               