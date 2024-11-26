from django.db import models

# Create your models here.

class Ventas(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    idproducto=models.CharField(max_length=50)
    idcliente=models.CharField(max_length=15)
    idsucursal=models.CharField(max_length=50)
    idempleado=models.CharField(max_length=25)
    total=models.CharField(max_length=100)
    fecha=models.CharField(max_length=50)
    cantidad=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.id