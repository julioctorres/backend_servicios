from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello ingreso a la pagina principal de las facturas, por favor seleccione a continuacion que desea hacer:")


def crear(request):
    return HttpResponse("¡A continuación podras crear una factura nueva!")


def actualizar(request):
    return HttpResponse("¡A continuacón actualizar una factura!")


def eliminar(request):
    return HttpResponse("¡A continuación podra eliminar una factura!")


def leer(request):
    return HttpResponse("¡A continuacion podemos observar la factura que desee!")