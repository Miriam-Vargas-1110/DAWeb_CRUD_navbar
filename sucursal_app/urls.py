from django.urls import path
from sucursal_app import views

urlpatterns = [

    path("sucursal", views.inicio_vistaSucursal,name="sucursal"),
    path("registrarsucursal/",views.registrarsucursal,name="registrarsucursal"),
    path("seleccionarsucursal/<id>",views.seleccionarsucursal,name="seleccionarsucursal"),
    path("editarsucursal/",views.editarsucursal,name="editarsucursal"),
    path("borrarsucursal/<id>",views.borrarsucursal,name="borrarsucursal"),
    
]