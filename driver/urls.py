from django.urls import path
from . views import  drivers, create_driver,single_driver,post_ratings

urlpatterns = [
    # path('drivers_dash/', drivers_dash, name='drivers_dash'),
    path("create_driver", create_driver, name="create_driver"), 
    path('drivers/', drivers, name='drivers'),
    path('drivers/<int:pk>', single_driver, name='single_driver'),
    path('rates/', view=post_ratings,name='post_ratings')
   
   
]