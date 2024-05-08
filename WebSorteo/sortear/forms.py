from django import forms
from .models import CategoriaPremio

class Formulario_Premio(forms.Form):
    nombre_premio=forms.CharField(max_length=50, label="Nombre del premio")
    categorias_premio = forms.ModelChoiceField(label='categoria', queryset=CategoriaPremio.objects.all())
    descripcion_premio= forms.CharField(widget=forms.Textarea(attrs={'row':5,'col':20}), label="Descripcion del premio")
    
    


class Formulario_Sorte(forms.Form):
    nombre_sorteo= forms.CharField(max_length=50, label="Nombre del Sorteo")
    descripcion_sorteo= forms.CharField(widget=forms.Textarea(), label="Descripcion del Sorteo")
    precio_sorteo = forms.FloatField(label="Precio del sorteo")
    
   
   
   




    

