from django import forms    
from .models import Cuadro, Escultura, Ceramica

class CuadroForm(forms.ModelForm):
    class Meta:
        Model = Cuadro
        fields = ['titulo', 'autor', 'descripcion', 'foto']

class EsculturaForm(forms.ModelForm):
    class Meta:
        Model = Escultura
        fields = ['titulo', 'autor', 'descripcion', 'foto']

class CeramicaForm(forms.ModelForm):
    class Meta:
        Model = Ceramica
        fields = ['titulo', 'autor', 'descripcion', 'foto']