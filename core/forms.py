from django import forms
from django.forms import ModelForm
from .models import EventoLibro
from django.core.exceptions import ValidationError

class EventoForm(ModelForm):
    # class Meta:
    #     model = EventoLibro
    #     fields = '__all__'
    class Meta:
        model = EventoLibro
        fields = ['evento']

    def clean_evento(self, *args, **kwargs):
        cleaned_data = super().clean()
        evento = self.cleaned_data['evento']
        print(evento)

        if len(str(self.cleaned_data['evento'])) < 5:
            raise forms.ValidationError(None, "Evento debe ser mayor a 5 caracteres")
            print("Error")
        return evento