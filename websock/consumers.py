import asyncio

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from send_location.models import Device, Location


class SendLocationConsumer(AsyncWebsocketConsumer):
     """send location

     Args:
         AsyncWebsocketConsumer (_type_): _description_
     """
     async def connect(self):
          """_summary_

          Returns:
              _type_: _description_
          """
          await self.accept()
          await self.send(text_data=f"hello")
          self.task = asyncio.create_task(self.send_data())
          return super().connect()
    
     async def disconnect(self, code):
          """_summary_

          Returns:
              _type_: _description_
          """
          if hasattr(self, "task"):
               self.task.cancel()
          return await super().disconnect(code)
     
     async def receive(self, text_data=None):
          """_summary_

          Returns:
              _type_: _description_
          """
          await self.send(text_data=text_data)
     
     async def send_data(self):
          """_summary_

          Returns:
              _type_: _description_
          """
          while True:
               devices = await sync_to_async(list)(Device.objects.all())
               locations = await sync_to_async(list)(Location.objects.all())
               for location_item in locations:
                    for device_item in devices:
                         if location_item.id == device_item.last_position_id :
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
