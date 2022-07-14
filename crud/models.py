from distutils.command.upload import upload
from hashlib import blake2b
from tabnanny import verbose
from django.db import models

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(max_length=50, verbose_name='Marca')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ['marca']

    def __str__(self):
        return self.marca

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True,max_length=20, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen', upload_to='productos',null=True, blank=True)
    descripcion = models.CharField(max_length=200, verbose_name='Descripción')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering=['id_producto']

    def __str__(self):
        return self