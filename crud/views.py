

from django.shortcuts import render,redirect,reverse
from django.http import HttpRequest
from .models import *
from .forms import *


# Create your views here.

def product_list(request):
    context = {'productos':Producto.objects.all()}
    return render(request, 'crud/product_list.html', context)

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            id_producto = form.cleaned_data.get("id_producto")
            nombre = form.cleaned_data.get("nombre")
            precio = form.cleaned_data.get("precio")
            stock = form.cleaned_data.get("stock")
            marca = form.cleaned_data.get("marca")
            imagen = form.cleaned_data.get("imagen")
            descripcion = form.cleaned_data.get("descripcion")
            obj = Producto.objects.create(
                id_producto=id_producto,
                nombre = nombre,
                precio=precio,
                stock=stock,
                imagen=imagen,
                descripcion=descripcion,
                marca=marca
            )
            obj.save()
            return redirect(reverse('product-new')+"?OK")
        else:
            return redirect(reverse('product-new')+"?FAIL")
    else:
        form = ProductForm
    return render(request,'crud/product_new.html',{'form':form})

def product_detail(request, product_id):
    try:
        producto = Producto.objects.get(id_producto=product_id)
        if producto:
            context = {'producto':producto}
            return render(request,'crud/product_detail.html',context)
    except:
        return redirect(reverse('product-list') + "?FAIL")
