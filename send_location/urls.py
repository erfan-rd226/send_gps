from django.urls import path 

from send_location import apis

app_name="send_location"

urlpatterns = [
    path("", apis.LocationApi.as_view(), name="create_location")
]
