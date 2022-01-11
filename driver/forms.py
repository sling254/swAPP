from django import forms
from django.forms.models import ModelForm
from .models import Driver



class DriversForm(ModelForm):
    
    class Meta:
        model = Driver
        fields =['name','photo', 'details' ,'location','charge','email', 'phone_number']