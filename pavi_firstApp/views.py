from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def fecha(request):
    dt=datetime.datetime.now()
    im="<title>Fecha y hora</title><h1>Imprimiendo la hora</h1><br><i>La Fecha y hora actual son: </i><br>"+str(dt)+"<br><p>Fecha y hora imprimidas..</p><footer>Gracias :)</footer>"
    return HttpResponse(im)

def saludo(request):
    s="<title>Saludo</title><h1>Hola :)</h1><h2>Solicitud</h2><label>Ingrese su nombre:</label><br><input></input><button>Enviar</button>"
    return HttpResponse(s)

