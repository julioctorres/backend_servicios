from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("¡Hola! estas en la pagina principal, que deseas hacer")


def ingreso(request):
    return HttpResponse("has seleccionado ingreso, por favor llenar las credenciales ")


def registro(request):
    return HttpResponse("has seleccionado registrar usuario, por favor llenar las credenciales ")


def ing_principal(request):
    return HttpResponse("has ingresado a la pagina principal, seleccione a continuacion lo que desea hacer: ")


def eliminar_usuario(request):
    return HttpResponse("Seleccione a continuación el usuario que desea eliminar")


def leer_usuarios(request):
    return HttpResponse("A continuacion se mostrara todos los usuarios ")


def actualizar_usuario(request):
    return HttpResponse("ingrese el nombre del usuario que desea actualizar")