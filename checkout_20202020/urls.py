# contiene las direcciones locales de la app checkout

from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import * 
#viewset: especificamos las rutas mediante routers


router = DefaultRouter()  #agrega direcciones de nuestros viewsets

router.register('carrito', CarritoAPI, basename = "carrito")

urlpatterns = [
    #lista de direcciones locales
    path('crud/', include(router.urls))
]