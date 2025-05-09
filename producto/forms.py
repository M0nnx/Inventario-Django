from django import forms
from .models import Producto, Categoria


class CategoriaForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Categoria
        fields = ['nombre','imagen']

class ProductoForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta: 
        model = Producto
        fields = ['nombre','descripcion','precio','stock','categoria','imagen']
        categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Selecciona una categoría")