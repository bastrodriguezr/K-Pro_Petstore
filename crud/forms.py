from dataclasses import fields
from django import forms
from django.forms import ModelForm, widgets
from .models import *

class ProductForm(ModelForm):

    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'nombre',
            'precio',
            'stock',
            'imagen',
            'descripcion',
            'marca'
        ]
        labels = {
            'id_producto':'Código Producto',
            'nombre':'Nombre Producto',
            'precio':'Precio',
            'stock':'Stock',
            'imagen':'Imagen',
            'descripcion':'Descripción',
            'marca':'Marca'
        }
        widgets = {
            'id_producto':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'stock':forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'imagen':forms.FileInput(attrs={'class':'form-control custom-file-input', 'lang':'es'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.Select(attrs={'class':'form-control'})
        }