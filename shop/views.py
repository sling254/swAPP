from django.http.response import JsonResponse
from django.shortcuts import render
import json

# Create your views here.


def IndexView(request):
    return render(request, 'home.html')


def ProductsView(request):
    return render(request, 'products.html')

def CheckoutView(request):
    return render(request, 'checkout.html')

def UpdateView(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']

    print('Action:',action)
    print('productId:', productId)
    return JsonResponse('item was added', safe=False)