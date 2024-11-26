from django.urls import path
from app_base import views

urlpatterns = [
    #inicio Tienda de ropa
    path('',views.inicio),
]
