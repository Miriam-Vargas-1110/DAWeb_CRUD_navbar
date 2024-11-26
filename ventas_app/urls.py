from django.urls import path
from ventas_app import views

urlpatterns = [
    path("ventas", views.inicio_vistaVentas,name="ventas"),
    path("registrarventas/",views.registrarventas,name="registrarventas"),
    path("seleccionarventas/<id>",views.seleccionarventas,name="seleccionarventas"),
    path("editarventas/",views.editarventas,name="editarventas"),
    path("borrarventas/<id>",views.borrarventas,name="borrarventas"),
    
]