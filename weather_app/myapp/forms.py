from django.forms import ModelForm, TextInput
from .models import City

class cityform (ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder':'Entr a city name'})}