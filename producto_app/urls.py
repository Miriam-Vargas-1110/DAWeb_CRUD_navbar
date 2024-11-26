from django.urls import path
from producto_app import views

urlpatterns = [
    path("productos", views.inicio_vistaProductos,name="productos"),
    path("registrarproductos/",views.registrarproductos,name="registrarproductos"),
    path("seleccionarproductos/<id>",views.seleccionarproductos,name="seleccionarproductos"),
    path("editarproductos/",views.editarproductos,name="editarproductos"),
    path("borrarproductos/<id>",views.borrarproductos,name="borrarproductos"),
    
]