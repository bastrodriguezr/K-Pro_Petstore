from django.urls import path

from .views import *

urlpatterns = [
    path('', root),
    path('home', home, name='home'),
    path('productos', productos, name='productos'),
    path('producto/<str:product_id>/', detalle_producto,name='product-detail'),
    path('contacto', contacto, name='contacto'),
    path('nosotros', nosotros, name="nosotros")
]