from re import template
from typing import Generic
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic 

from . import services as s
from . import models as m
# Create your views here.

def index(request):
    return HttpResponse("¡Hola! estas en la pagina principal, que deseas hacer")


def ingreso(request):
    
    return HttpResponse("has seleccionado ingreso, por favor llenar las credenciales ")


class registro(generic.TemplateView):
    model = m.Client
    template_name = "cliente/registro_cliente.html"

class IngPrincipal(generic.View):
    def get(self, request):
        data = s.descargar_formato()
        response = HttpResponse(data.export('xlsx'), content_type='application/vnd.ms-excel')
        response ["Conten-Disposition"] = 'attachment; filename=formato_de_cargue_archivos.xlsx'
        return response 
    
    

def eliminar_usuario(request):
    return HttpResponse("Seleccione a continuación el usuario que desea eliminar")


def leer_usuarios(request):
    return HttpResponse("A continuacion se mostrara todos los usuarios ")


def actualizar_usuario(request):
    return HttpResponse("ingrese el nombre del usuario que desea actualizar")