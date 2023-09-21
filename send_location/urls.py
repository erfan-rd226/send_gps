from django.urls import path 

from . import views 


urlpatterns = [
    path("",views.SendLocationViewSet.as_view())
]
