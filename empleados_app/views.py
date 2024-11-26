from django.shortcuts import render,redirect
from .models import Empleados


def inicio_vistaEmpleados(request):
    losempleados=Empleados.objects.all()

    return render(request,"gestionarempleados.html",{"misempleados":losempleados})

def registrarempleados(request):
    id=request.POST["txtid"]
    nombres=request.POST["txtnombres"]
    apellidos=request.POST["txtapellidos"]
    numero=request.POST["skznumero"]
    cargo=request.POST["skzcargo"]
    salario=request.POST["skzsalario"]
    horario=request.POST["skzhorario"]

    guardarempleados=Empleados.objects.create(id=id,nombres=nombres,apellidos=apellidos,numero=numero,cargo=cargo,salario=salario,horario=horario)

    return redirect('empleados') 

def seleccionarempleados(request,id):
    
    empleados=Empleados.objects.get(id=id)
    return render(request,"editarempleados.html",{"misempleados":empleados})

def editarempleados(request):
    id=request.POST["txtid"]
    nombres=request.POST["txtnombres"]
    apellidos=request.POST["txtapellidos"]
    numero=request.POST["skznumero"]
    cargo=request.POST["skzcargo"]
    salario=request.POST["skzsalario"]
    horario=request.POST["skzhorario"]

    emp=Empleados.objects.get(id=id)
    emp.nombres=nombres
    emp.apellidos=apellidos
    emp.numero=numero
    emp.cargo=cargo
    emp.salario=salario
    emp.horario=horario
    emp.save()
    return redirect('empleados') 

def borrarempleados(request,id):
    empleado=Empleados.objects.get(id=id)
    empleado.delete()
    return redirect("empleados")

# Create your views here.

