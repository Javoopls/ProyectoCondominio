from django import forms
from django.forms import ModelForm
from .models import EventoLibro

class EventoForm(ModelForm):
    # class Meta:
    #     model = EventoLibro
    #     fields = '__all__'
    class Meta:
        model = EventoLibro
        fields = ['evento']