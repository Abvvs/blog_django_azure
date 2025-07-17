from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe tu comentario...'}),
        }
        labels = {
            'autor': 'Nombre',
            'texto': 'Comentario',
        }