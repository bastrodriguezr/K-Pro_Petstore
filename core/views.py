from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from crud.models import *

# Create your views here.

def root(request):
    return redirect('/home')

def home(request):
    return render(request, 'core/home.html')

def productos(request):
    context = {'productos':Producto.objects.all()}
    return render(request, 'core/productos.html', context)

def detalle_producto(request, product_id):
    try:
        producto = Producto.objects.get(id_producto=product_id)
        if producto:
            context = {'producto':producto}
            return render(request,'core/detalle_producto.html',context)
    except:
        return redirect(reverse('productos') + "?FAIL")

def nosotros(request):
    return render(request, 'core/nosotros.html')

def contacto(request):
    return render(request, 'core/contacto.html')