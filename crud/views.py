
from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest


# Create your views here.

def product_list(request):
    return render(request, 'crud/product_list.html')

def product_new(request):
    return render(request,'crud/product_new.html')
