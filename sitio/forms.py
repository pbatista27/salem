"""formularios"""

from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'apellido', 'correo', 'asunto', 'mensaje')
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'asunto': 'Asunto',
            'correo': 'Correo',
            'mensaje': 'Mensaje'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduzca Nombre'
                }),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Intruduzca Apellido'
                }),
            'asunto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Intrduzca Asunto'
                }),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduzca Correo'
                }),
            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite Mensaje',
                })
        }



