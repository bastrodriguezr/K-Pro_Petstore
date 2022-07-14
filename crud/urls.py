from django.urls import path

from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('new/', product_new, name='product_new')
]