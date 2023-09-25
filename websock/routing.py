
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("erfan/", consumers.SendLocationConsumer.as_asgi(), name="PracticeConsumer"),
]
