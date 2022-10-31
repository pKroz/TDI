from django.shortcuts import render
from .models import *
from django.template.loader import *
from django.template import *
from django.http import *
import mimetypes
# Create your views here.
def inicio(request):
    testimoniosListados = testimonios.objects.all()[:9]
    return render(request,"inicio.html", {"testimonios": testimoniosListados})
def pCursos(request):
    cursosListados = cursos.objects.all()
    return render(request,"cursos.html", {"cursos": cursosListados})
def pWorkshops(request):
    workshopsListados = workshops.objects.all()
    return render(request,"workshops.html", {"workshops": workshopsListados})
def pMern(request):
    cursosListados = cursos.objects.all().filter(titulo="MERN")
    return render(request,"cursos/mern.html", {"cursos": cursosListados})
def pDesarrolloWEB(request):
    cursosListados = cursos.objects.all().filter(titulo="Desarrollo Web")
    return render(request,"cursos/desarrolloweb.html", {"cursos": cursosListados})
def pCompra(request):
    return render(request,"compra.html", {})