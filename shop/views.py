from django.shortcuts import render

# Create your views here.


def IndexView(request):
    return render(request, 'home.html')


def ProductsView(request):
    return render(request, 'products.html')
