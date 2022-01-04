from django.urls import path
from . import views

urlpatterns = [
    path('', views.drivers_dash, name='drivers-dashboard'),
   
]