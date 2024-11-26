from django.shortcuts import render,redirect
from .models import Producto


def inicio_vistaProductos(request):
    losproductos=Producto.objects.all()

    return render(request,"gestionarproductos.html",{"misproductos":losproductos})

def registrarproductos(request):
    id=request.POST["txtid"]
    idprovedor=request.POST["txtidprovedor"]
    nombre=request.POST["txtnombre"]
    categoria=request.POST["skzcategoria"]
    precio=request.POST["skzprecio"]
    descripcion=request.POST["skzdescripcion"]
    marca=request.POST["skzmarca"]
    idsucursal=request.POST["skzidsucursal"]

    guardarproductos=Producto.objects.create(id=id,idprovedor=idprovedor,nombre=nombre,categoria=categoria,precio=precio,descripcion=descripcion,marca=marca,idsucursal=idsucursal)

    return redirect('productos') 

def seleccionarproductos(request,id):
    
    productos=Producto.objects.get(id=id)
    return render(request,"editarproductos.html",{"misproductos":productos})

def editarproductos(request):
    id=request.POST["txtid"]
    idprovedor=request.POST["txtidprovedor"]
    nombre=request.POST["txtnombre"]
    categoria=request.POST["skzcategoria"]
    precio=request.POST["skzprecio"]
    descripcion=request.POST["skzdescripcion"]
    marca=request.POST["skzmarca"]
    idsucursal=request.POST["skzidsucursal"]

    pro=Producto.objects.get(id=id)
    pro.idprovedor=idprovedor
    pro.nombre=nombre
    pro.categoria=categoria
    pro.precio=precio
    pro.descripcion=descripcion
    pro.marca=marca
    pro.idsucursal=idsucursal
    pro.save()
    return redirect('productos') 

def borrarproductos(request,id):
    productoss=Producto.objects.get(id=id)
    productoss.delete()
    return redirect("productos")

# Create your views here.