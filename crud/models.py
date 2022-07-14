from distutils.command.upload import upload
from hashlib import blake2b
from tabnanny import verbose
from django.db import models

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(max_length=50, verbose_name='Marca')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ['marca']

    def __str__(self):
        return self.marca

