from django.db import models

# Create your models here.

class Clientes(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=15)
    numero=models.CharField(max_length=50)
    direccion=models.CharField(max_length=25)
    correo=models.CharField(max_length=100)
    estado=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    codigop=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.nombres