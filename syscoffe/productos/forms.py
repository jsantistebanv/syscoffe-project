from django import forms
from .models import Categoria, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre', )


class ProductoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False, max_length=50)
    
    class Meta:
        model = Producto
        fields = ('nombre', 'categoria', 'precio', 'descripcion', 'imagen')
    
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise forms.ValidationError("El precio no puede ser menor a 0")
        return precio
