from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.


def IndexView(request):
    return render(request, 'home.html')


def ProductsView(request):
    return render(request, 'products.html')

def CheckoutView(request):
    return render(request, 'checkout.html')

def UpdateView(request):
    return JsonResponse({'status': 'ok'}, safe=False)