from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Folios
from django.db.models import query

# Create your views here.
#MVT modelo vista template o modelo template vista

def index(request):

    return render(request, 'index.html')

def login(request):

    return render(request, 'login.html')

def crear_formulario(request):

    return render(request,'articulos.html')

def save_folio (request):
    folios = Folios(
        
        area = area,
        objeto = objeto,
        valor = valor,
        contenido = content,

    )
    folios.save()
    return HttpResponse("Se envio tu solicitud")
