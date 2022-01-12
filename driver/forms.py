from django import forms
from django.forms.models import ModelForm
from .models import Driver
from django.forms.widgets import Textarea



class DriversForm(ModelForm):
    
    class Meta:
        model = Driver

        fields =['name','photo', 'details' ,'location','charge','email', 'phone_number']
        widgets = {
            'details': Textarea(attrs={'cols' : 20, 'rows' : 3}),
        }
