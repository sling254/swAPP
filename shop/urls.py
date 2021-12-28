from django.urls import path
from .views import IndexView,ProductsView,CheckoutView,UpdateView

urlpatterns = [
    path('', IndexView, name='index'),
    path('products/', ProductsView, name='products'),
    path('checkout/', CheckoutView, name='checkout'),
    path('UpdateItem/', UpdateView, name='UpdateItem'),
   
]