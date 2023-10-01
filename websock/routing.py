
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("send_position/", consumers.SendLocationConsumer.as_asgi()),
]
