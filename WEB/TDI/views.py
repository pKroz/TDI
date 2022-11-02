from django.shortcuts import redirect, render
from .models import *
from django.template.loader import *
from django.template import *
from django.http import *
from django.contrib import messages
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
    cursosListados = cursos.objects.all()
    if request.method =='POST':
        c = pagos()
        c.dni = request.POST.get('dni')
        c.nombres = request.POST.get('nombres')
        c.apellidos  = request.POST.get('apellidos')
        c.correo = request.POST.get('correo')
        c.celular = request.POST.get('celular')
        c.curso = request.POST.get('curso')
        c.medio = request.POST.get('medio')
        c.voucher = request.POST.get('voucher')
        c.save()
        return redirect('/gracias')
    return render(request,"compra.html", {"cursos": cursosListados})
    