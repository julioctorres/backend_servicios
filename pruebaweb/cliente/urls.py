from django.urls import path 
from . import views



urlpatterns = [
    path("index", views.index, name = "index" ),
    path("ingreso", views.ingreso, name = "ingreso" ),
    path("registro", views.registro, name = "registro" ),
    path("ing_principal", views.IngPrincipal.as_view(), name = "ing_principal" ),
    path("eliminar_usuario", views.eliminar_usuario, name = "eliminar_usuario" ),
    path("leer_usuarios", views.leer_usuarios, name = "leer_usuarios" ),
    path("actualizar_usuario", views.actualizar_usuario, name = "actualizar_usuario" ),
    path("cargue_descargue", views.CargueDescargue, name = "cargue_descargue" ), 
    
    ]