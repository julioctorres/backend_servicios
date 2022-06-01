from django.shortcuts import render
from django.http import HttpResponse

from . import models as m

# Create your views here.
def index(request):
    return HttpResponse("Hello ingreso a la pagina principal de los productos, por favor seleccione a continuacion que desea hacer:")


def crear(request):
    return HttpResponse("¡A continuación podras crear un nuevo producto nueva!")


def actualizar(request):
    return HttpResponse("¡A continuacón actualizar el informe de un producto!")


def eliminar(request):
    return HttpResponse("¡A continuación podra eliminar  un producto !")


def leer(request):
    productos_activos = m.Product.objects.all()
    return render(request, "productos/leer.html", {"productos": productos_activos})