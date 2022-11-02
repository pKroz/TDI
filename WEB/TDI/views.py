from django.shortcuts import redirect, render
from .models import *
from .forms import *
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
    if request.method =='POST':
        dni = request.POST['dni']
        nombres = request.POST['nombres']
        apellidos  = request.POST['apellidos']
        correo = request.POST['correo']
        celular = request.POST['celular']
        curso = request.POST['curso']
        medio = request.POST['medio']
        

        nueva_compra = pagos(dni=dni, nombres=nombres, apellidos=apellidos,correo=correo
        , celular=celular, curso=curso, medio=medio,)
        nueva_compra.save()
    return render(request,"compra.html", {})
    