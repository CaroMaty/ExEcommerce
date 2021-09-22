from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, FloatField, IntegerField
from django.db.models.fields.json import DataContains
from django.db.models.fields.related import ForeignKey
from Productos.models import Producto

# Create your models here.

class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.FloatField(default=0)
    pagado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.usuario + " - " + str(self.fecha)
    
    def total(self):
        pass

    def numArt(self):
        pass

class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.carrito.__str__()

class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + " / " + self.producto.__str__()
    
    def subtotal(self):
        return self.cantidad * self.producto.precio
