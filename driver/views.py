from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
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
    
    return render(request,'single_driver.html',{'drivers': drivers,'current_user':current_user,})