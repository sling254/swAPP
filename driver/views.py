from django.shortcuts import render

# Create your views here.
def drivers_dash(request):
    return render(request,'dashboard.html')