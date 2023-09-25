from django.urls import path 

from . import views 


urlpatterns = [
    path("",views.LocationApi.as_view())
]
