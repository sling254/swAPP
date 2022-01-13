from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import Customer, OrderItem, Product, Order

# Create your views here.


def IndexView(request):
    return render(request, 'home.html')


def ProductsView(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer  = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart-total':0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order':order,
        'products':products
    }
    return render(request, 'products.html', context)

def CheckoutView(request):
    if request.user.is_authenticated:
        customer  = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart-total':0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order':order
    }
    return render(request, 'checkout.html',context)
def CartView(request):
    if request.user.is_authenticated:
        customer  = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart-total':0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order':order
    }
    return render(request, 'cart.html',context)

def UpdateView(request):
    data= json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("Hello")
    print('Action:', action)
    print('ProductId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()



    return JsonResponse('item was added', safe=False)