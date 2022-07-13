from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def root(request):
    return redirect('/home')

def home(request):
    return render(request, 'core/home.html')
