from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Driver, Rating
from django.forms.widgets import Textarea



class DriversForm(ModelForm):
    
    class Meta:
        model = Driver

        fields =['name','photo', 'details' ,'charge','email', 'phone_number']
        widgets = {
            'details': Textarea(attrs={'cols' : 20, 'rows' : 3}),
        }


class RatesForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['efficiency_rate','service_rate','avarage_rate']