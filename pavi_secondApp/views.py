from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def texto(request):
    tex="<title>Texto</title><h1>Imprimiendo Texto</h1><br><i>Cursiva</i><br><b>Negrita</b><br><u>Subrayado</u><br><strong>IMPORTANTE</strong>"
    return HttpResponse(tex)

def listas(request):
    lista="<title>Listas</title><h3>Lista númerada</h3><ol><li>Saludar</li><li>Ingresar</li><li>Despedir</li></ol><h3>Lista sin orden</h3><ul><li>A</li><li>S</li></ul>"
    return HttpResponse(lista)