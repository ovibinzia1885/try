from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, Select, FileInput

from .models import service

STATUS = [
		("engin", "engin"),
		("wash", "wash"),
		("glass", "glass"),
		("breakplate", "breakplate"),
	]

BIKE = (
		("R15", "R15"),
		("Hero", "Hero"),
		("yamma", "yamma"),
	)

class ServiceForm(forms.ModelForm):
    class Meta:
        model =service
        fields = ('phone', 'type', 'bike_type')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'Type': Select(attrs={'class': 'input', 'placeholder': 'Type'}, choices=STATUS),
            'bike_type': Select(attrs={'class': 'input', 'placeholder': 'bike_type'}, choices=BIKE),
        }