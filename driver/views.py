from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from driver.forms import *
from driver.models import *

# Create your views here.
# def drivers_dash(request):

#     drivers = Driver.objects.all().order_by('-id')

#     return render(request,'dashboard.html', {"drivers": drivers})



def create_driver(request):
    current_user = request.user
    if request.method == "POST":
        
        form=DriversForm(request.POST,request.FILES)

        if form.is_valid():
            drivers=form.save(commit=False)
            drivers.user=current_user
            
            drivers.save()
        return HttpResponseRedirect('/drivers/drivers')
    else:
        form=DriversForm()
    return render (request,'driver_form.html', {'form': form})


def drivers(request):
   
    
    drivers = Driver.objects.all().order_by('-id')
    
    return render(request, "dashboard.html", {"drivers": drivers})


def single_driver(request,name):
    current_user = request.user
    drivers = Driver.objects.get(name=name)
    ratings = Rating.objects.all().order_by('-id')
    
    
    return render(request,'single_driver.html',{'ratings':ratings, 'current_user':current_user,"drivers": drivers})

# def post_ratings(request):
#     if request.method == "POST":
        
        
#         form = RatesForm(request.POST,request.FILES)

#         if form.is_valid():
            
#             form.save(commit=False)
            
#             return render(request,'single_driver.html')
#     else:
#         form=RatesForm()
#     return render (request,'ratings.html', {'form': form})
        

def ratings(request):
   
    
    ratings = Rating.objects.all().order_by('-id')
    
    return render(request, "single_driver.html", {"ratings": ratings})

def rate(request,id):
    if request.method == 'POST':
        drivers = Driver.objects.get(id = id)
        current_user = request.user
        efficieny_rate = request.POST['efficiency']
        service_rate = request.POST['service']
        

        Rating.objects.create(
            
            user=current_user,
            efficiency_rate=efficieny_rate ,
            service_rate=service_rate,
            avarage_rate=round((float(efficieny_rate )+float(service_rate))/2,1),)

        return render(request,"single_driver.html",{"drivers":drivers})
    else:
        drivers = Driver.objects.get(id = id) 
        return render(request,"single_driver.html",{"drivers":drivers})



