from django.db import models

# Create your models here.

class Empleados(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=15)
    numero=models.CharField(max_length=50)
    cargo=models.CharField(max_length=25)
    salario=models.IntegerField()
    horario=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.nombres