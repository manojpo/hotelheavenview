
from django.forms import forms
from django.forms import ModelForm
from .models import *


class RoomForm(forms.Form):
    class meta:
        model = Room
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'roomcode':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),




    }
        fields = "__all__"

