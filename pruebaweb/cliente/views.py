import email
from re import template
from typing import Generic
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm

from . import services as s
from . import models as m

# Create your views here.

def index(request):
    model = m.Client
    return render(request, "cliente/index.html")

def ingreso(request):
    return render(request, "cliente/ingreso.html")
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            firts_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['username']
            password = form.cleaned_data['username']
    else:
            form = UserCreationForm()

    context = {'form': form}    
    return render(request,'cliente/registro_cliente.html')


def CargueDescargue(request):
    
    return render(request, "cliente/cargue_descargue.html")

class IngPrincipal(generic.View):
    def get(self, request):
        data = s.descargar_formato()
        response = HttpResponse(data.export('xlsx'), content_type='application/vnd.ms-excel')
        response ["Conten-Disposition"] = 'attachment; filename=formato_de_cargue_archivos.xlsx'
        return response 
    
    

def eliminar_usuario(request):
    return HttpResponse("Seleccione a continuación el usuario que desea eliminar")


def leer_usuarios(request):
    clientes_activos = m.Client.objects.all()
    return render(request, "cliente/leer_usuarios.html", {"clientes": clientes_activos})


def actualizar_usuario(request):
    return HttpResponse("ingrese el nombre del usuario que desea actualizar")