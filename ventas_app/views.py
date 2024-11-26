from django.shortcuts import render,redirect
from .models import Ventas


def inicio_vistaVentas(request):
    lasventas=Ventas.objects.all()

    return render(request,"gestionarventas.html",{"misventas":lasventas})

def registrarventas(request):
    id=request.POST["txtid"]
    idproducto=request.POST["txtidproducto"]
    idcliente=request.POST["txtidcliente"]
    idsucursal=request.POST["skzidsucursal"]
    idempleado=request.POST["skzidempleado"]
    total=request.POST["skztotal"]
    fecha=request.POST["skzfecha"]
    cantidad=request.POST["skzcantidad"]

    guardarventas=Ventas.objects.create(id=id,idproducto=idproducto,idcliente=idcliente,idsucursal=idsucursal,idempleado=idempleado,total=total,fecha=fecha,cantidad=cantidad)

    return redirect('ventas') 

def seleccionarventas(request,id):
    
    ventas=Ventas.objects.get(id=id)
    return render(request,"editarventas.html",{"misventas":ventas})

def editarventas(request):
    id=request.POST["txtid"]
    idproducto=request.POST["txtidproducto"]
    idcliente=request.POST["txtidcliente"]
    idsucursal=request.POST["skzidsucursal"]
    idmpleado=request.POST["skzidempleado"]
    total=request.POST["skztotal"]
    fecha=request.POST["skzfecha"]
    cantidad=request.POST["skzcantidad"]

    ven=Ventas.objects.get(id=id)
    ven.idproducto=idproducto
    ven.idcliente=idcliente
    ven.idsucursal=idsucursal
    ven.idempleado=idmpleado
    ven.total=total
    ven.fecha=fecha
    ven.cantidad=cantidad
    ven.save()
    return redirect('ventas') 

def borrarventas(request,id):
    ventass=Ventas.objects.get(id=id)
    ventass.delete()
    return redirect("ventas")

# Create your views here.