from django.urls import path
from .views import IndexView,ProductsView,CheckoutView,UpdateView,CartView, suppliersView

urlpatterns = [
    path('', IndexView, name='index'),
    path('products/', ProductsView, name='products'),
    path('checkout/', CheckoutView, name='checkout'),
    path('suppliers/' ,suppliersView,name='suppliers'),
    path('update_item/', UpdateView, name='update_item'),
    path('cart/', CartView, name='cart'),
   
]