from django.urls import path
from provedores_app import views

urlpatterns = [
    path("provedores", views.inicio_vistaProvedores,name="provedores"),
    path("registrarprovedores/",views.registrarprovedores,name="registrarprovedores"),
    path("seleccionarprovedores/<id>",views.seleccionarprovedores,name="seleccionarprovedores"),
    path("editarprovedores/",views.editarprovedores,name="editarprovedores"),
    path("borrarprovedores/<id>",views.borrarprovedores,name="borrarprovedores"),
    
]