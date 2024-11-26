from django.shortcuts import render,redirect
from .models import Clientes


def inicio_vistaClientes(request):
    losclientes=Clientes.objects.all()

    return render(request,"gestionarclientes.html",{"misclientes":losclientes})

def registrarclientes(request):
    id=request.POST["txtid"]
    nombres=request.POST["txtnombres"]
    apellidos=request.POST["txtapellidos"]
    numero=request.POST["txtnumero"]
    direccion=request.POST["skzdireccion"]
    correo=request.POST["skzcorreo"]
    estado=request.POST["skzestado"]
    ciudad=request.POST["skzciudad"]
    codigop=request.POST["skzcodigop"]

    guardarclientes=Clientes.objects.create(id=id,nombres=nombres,apellidos=apellidos,numero=numero,direccion=direccion,correo=correo,estado=estado,ciudad=ciudad,codigop=codigop)

    return redirect('clientes') 

def seleccionarclientes(request,id):
    
    cliente=Clientes.objects.get(id=id)
    return render(request,"editarclientes.html",{"misclientes":cliente})

def editarclientes(request):
    id=request.POST["txtid"]
    nombres=request.POST["txtnombres"]
    apellidos=request.POST["txtapellidos"]
    numero=request.POST["txtnumero"]
    direccion=request.POST["skzdireccion"]
    correo=request.POST["skzcorreo"]
    estado=request.POST["skzestado"]
    ciudad=request.POST["skzciudad"]
    codigop=request.POST["skzcodigop"]

    cli=Clientes.objects.get(id=id)
    cli.nombres=nombres
    cli.apellidos=apellidos
    cli.numero=numero
    cli.direccion=direccion
    cli.correo=correo
    cli.estado=estado
    cli.ciudad=ciudad
    cli.codigop=codigop
    cli.save()
    return redirect('clientes') 

def borrarclientes(request,id):
    clientee=Clientes.objects.get(id=id)
    clientee.delete()
    return redirect("clientes")

# Create your views here.