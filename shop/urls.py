from django.urls import path
from .views import IndexView,ProductsView

urlpatterns = [
    path('', IndexView, name='index'),
    path('products/', ProductsView, name='products'),
   
]