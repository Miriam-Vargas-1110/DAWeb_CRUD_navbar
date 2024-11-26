from django.shortcuts import render,redirect
from .models import Sucursal

def inicio_vistaSucursal(request):
    lassucursales=Sucursal.objects.all()

    return render(request,"gestionarsucursal.html",{"missucursales":lassucursales})

def registrarsucursal(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    numero=request.POST["skznumero"]
    idempleados=request.POST["skzidempleados"]
    horario=request.POST["skzhorario"]
    correo=request.POST["skzcorreo"]

    guardarsucursal=Sucursal.objects.create(id=id,nombre=nombre,direccion=direccion,numero=numero,idempleados=idempleados,horario=horario,correo=correo)

    return redirect('sucursal') 

def seleccionarsucursal(request,id):
    
    sucursal=Sucursal.objects.get(id=id)
    return render(request,"editarsucursal.html",{"missucursales":sucursal})

def editarsucursal(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    numero=request.POST["skznumero"]
    idempleados=request.POST["skzidempleados"]
    horario=request.POST["skzhorario"]
    correo=request.POST["skzcorreo"]

    suc=Sucursal.objects.get(id=id)
    suc.nombre=nombre
    suc.direccion=direccion
    suc.numero=numero
    suc.idempleados=idempleados
    suc.horario=horario
    suc.correo=correo
    suc.save()
    return redirect('sucursal') 

def borrarsucursal(request,id):
    sucursall=Sucursal.objects.get(id=id)
    sucursall.delete()
    return redirect("sucursal")

# Create your views here.