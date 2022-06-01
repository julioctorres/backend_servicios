from django.shortcuts import render
from django.http import HttpResponse

from . import models as m

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
    facturas_activas = m.Bill.objects.all()
    return render(request, "facturas/leer.html", {"facturas": facturas_activas})