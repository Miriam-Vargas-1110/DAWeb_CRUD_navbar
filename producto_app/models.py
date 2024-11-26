from django.db import models

# Create your models here.

class Producto(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    idprovedor=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    categoria=models.CharField(max_length=15)
    precio=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=25)
    marca=models.CharField(max_length=100)
    idsucursal=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.nombre