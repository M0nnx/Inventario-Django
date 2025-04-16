from django import forms
from .models import Producto, Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = ['nombre','descripcion','precio','stock','categoria']
        categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Selecciona una categoría")