from django.urls import path
from empleados_app import views

urlpatterns = [
    path("empleados", views.inicio_vistaEmpleados,name="empleados"),
    path("registrarempleados/",views.registrarempleados,name="registrarempleados"),
    path("seleccionarempleados/<id>",views.seleccionarempleados,name="seleccionarempleados"),
    path("editarempleados/",views.editarempleados,name="editarempleados"),
    path("borrarempleados/<id>",views.borrarempleados,name="borrarempleados"),
    
]