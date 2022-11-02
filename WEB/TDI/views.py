from django.shortcuts import redirect, render
from .models import *
from django.template.loader import *
from django.template import *
from django.http import *
from django.contrib import messages
import datetime
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
    if request.method =='POST':
        com = comentarios()
        com.nombre = request.POST.get('nombre')
        com.comentario  = request.POST.get('comentario')
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        if len(str(day)) == 1 :
            day = "0" + str(day)
        if len(str(month)) == 1 :
            month = "0" + str(month)
        com.dia = day
        com.mes = month
        com.anio = year
        com.save()
        return redirect('/gracias')
    return render(request,"cursos/mern.html", {"cursos": cursosListados})

def pDesarrolloWEB(request):
    cursosListados = cursos.objects.all().filter(titulo="Desarrollo Web")
    if request.method =='POST':
        com = comentarios()
        com.nombre = request.POST.get('nombre')
        com.comentario  = request.POST.get('comentario')
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        if len(str(day)) == 1 :
            day = "0" + str(day)
        if len(str(month)) == 1 :
            month = "0" + str(month)
        com.dia = day
        com.mes = month
        com.anio = year
        com.save()
        return redirect('/gracias')
    return render(request,"cursos/desarrollo-web.html", {"cursos": cursosListados})

def pFundamentosAWS(request):
    cursosListados = cursos.objects.all().filter(titulo="Fundamentos de AWS")
    if request.method =='POST':
        com = comentarios()
        com.nombre = request.POST.get('nombre')
        com.comentario  = request.POST.get('comentario')
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        if len(str(day)) == 1 :
            day = "0" + str(day)
        if len(str(month)) == 1 :
            month = "0" + str(month)
        com.dia = day
        com.mes = month
        com.anio = year
        com.save()
        return redirect('/gracias')
    return render(request,"cursos/fundamentos-aws.html", {"cursos": cursosListados})

def pCompra(request):
    cursosListados = cursos.objects.all()
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if len(str(day)) == 1 :
        day = "0" + str(day)
    if len(str(month)) == 1 :
        month = "0" + str(month)
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
        c.dia = day
        c.mes = month
        c.anio = year
        c.save()
        return redirect('/gracias')
    return render(request,"compra.html", {"cursos": cursosListados})
    