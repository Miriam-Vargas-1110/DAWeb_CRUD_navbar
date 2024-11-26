from django.db import models

# Create your models here.

class Sucursal(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=15)
    direccion=models.CharField(max_length=50)
    numero=models.CharField(max_length=50)
    idempleados=models.CharField(max_length=25)
    horario=models.CharField(max_length=100)
    correo=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.nombre