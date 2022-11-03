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

def pBlogs(request):
    blogsListados = blogs.objects.all()
    return render(request,"blogs.html", {"blogs": blogsListados})

def pWorkshops(request):
    workshopsListados = workshops.objects.all()
    return render(request,"workshops.html", {"workshops": workshopsListados})

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

def pPostular(request):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if len(str(day)) == 1 :
        day = "0" + str(day)
    if len(str(month)) == 1 :
        month = "0" + str(month)
    if request.method =='POST':
        p = postulaciones()
        p.nombres = request.POST.get('nombres')
        p.apellidos  = request.POST.get('apellidos')
        p.correo = request.POST.get('correo')
        p.celular = request.POST.get('celular')
        p.sitio = request.POST.get('sitio')
        p.comentario = request.POST.get('comentario')
        p.puesto = request.POST.get('puesto')
        p.cv = request.POST.get('cv')
        p.dia = day
        p.mes = month
        p.anio = year
        p.save()
        return redirect('/gracias')
    return render(request,"trabaja-con-nosotros.html", {})

def pTerminos(request):
    return render(request,"terminos-y-condiciones.html", {})

def pNosotros(request):
    return render(request,"nosotros.html", {})

def pPreguntas(request):
    return render(request,"preguntas-frecuentes.html", {})

def pPoliticas(request):
    return render(request,"politicas-de-privacidad.html", {})

def pComunidad(request):
    return render(request,"comunidad.html", {})

def pGracias(request):
    return render(request,"gracias.html", {})

def pBecas(request):
    return render(request,"becas.html", {})

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

def pDictarWorkshop(request):
    if request.method =='POST':
        dw = dictar_workshop()
        dw.nombres = request.POST.get('nombres')
        dw.apellidos  = request.POST.get('apellidos')
        dw.correo  = request.POST.get('correo')
        dw.celular  = request.POST.get('celular')
        dw.area  = request.POST.get('area')
        dw.otro  = request.POST.get('otro')
        dw.cv  = request.POST.get('cv')
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        if len(str(day)) == 1 :
            day = "0" + str(day)
        if len(str(month)) == 1 :
            month = "0" + str(month)
        dw.dia = day
        dw.mes = month
        dw.anio = year
        dw.save()
        return redirect('/gracias')
    return render(request,"dictar-workshop.html", {})

def pDictarCurso(request):
    if request.method =='POST':
        dc = dictar_curso()
        dc.nombres = request.POST.get('nombres')
        dc.apellidos  = request.POST.get('apellidos')
        dc.correo  = request.POST.get('correo')
        dc.celular  = request.POST.get('celular')
        dc.area  = request.POST.get('area')
        dc.otro  = request.POST.get('otro')
        dc.cv  = request.POST.get('cv')
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        if len(str(day)) == 1 :
            day = "0" + str(day)
        if len(str(month)) == 1 :
            month = "0" + str(month)
        dc.dia = day
        dc.mes = month
        dc.anio = year
        dc.save()
        return redirect('/gracias')
    return render(request,"dictar-curso.html", {})


def pBlog1(request):
    blogsListados = blogs.objects.all().filter(id="1")
    return render(request,"blogs/herramientas-que-todo-desarrollador-web-deberia-conocer-en-el-2021.html", {"blogs": blogsListados})