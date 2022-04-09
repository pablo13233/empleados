from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo', 
            'subtitulo', 
            'cantidad'
        )
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese el Titulo'}),
            'subtitulo': forms.TextInput(attrs={'placeholder': 'Ingrese el SubTitulo'}),
            'cantidad': forms.NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
        }
        labels = {
            'titulo': 'Titulo',
            'subtitulo': 'Subtitulo',
            'cantidad': 'Cantidad',
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 0:
            raise forms.ValidationError("La cantidad no puede ser negativa")
        return cantidad
