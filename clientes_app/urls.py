from django.urls import path
from clientes_app import views

urlpatterns = [
    path("clientes", views.inicio_vistaClientes,name="clientes"),
    path("registrarclientes/",views.registrarclientes,name="registrarclientes"),
    path("seleccionarclientes/<id>",views.seleccionarclientes,name="seleccionarclientes"),
    path("editarclientes/",views.editarclientes,name="editarclientes"),
    path("borrarclientes/<id>",views.borrarclientes,name="borrarclientes"),
    
]