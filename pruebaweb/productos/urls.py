from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name = "index" ),
    path("crear", views.crear, name = "crear" ),
    path("actualizar", views.actualizar, name = "actualizar" ),
    path("eliminar", views.eliminar, name = "eliminar" ),
    path("leer", views.leer, name = "leer" )
] 