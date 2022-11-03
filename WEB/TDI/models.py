from django.db import models
import datetime
import os

# Create your models here.

class testimonios(models.Model):
    nombre = models.CharField(max_length=5000)
    comentario = models.CharField(max_length=5000)

class cursos(models.Model):
    banner = models.CharField(max_length=5000)
    banneralt = models.CharField(max_length=5000)
    docente  = models.CharField(max_length=5000)
    docentefoto = models.CharField(max_length=5000)
    docentealt = models.CharField(max_length=5000)
    cargo = models.CharField(max_length=5000)
    titulo = models.CharField(max_length=5000)
    categoria = models.CharField(max_length=5000)
    modalidad = models.CharField(max_length=5000)
    duracion = models.CharField(max_length=5000)
    clases = models.CharField(max_length=5000)
    horasClase = models.CharField(max_length=5000)
    horasTotal = models.CharField(max_length=5000)
    horario = models.CharField(max_length=5000)
    dias = models.CharField(max_length=5000)
    calificacion = models.CharField(max_length=5000)
    alumnos = models.CharField(max_length=5000)
    descuento = models.CharField(max_length=5000)
    precioOriginal = models.CharField(max_length=5000)
    precioActual = models.CharField(max_length=5000)
    descripcion = models.CharField(max_length=5000)
    url = models.CharField(max_length=5000)
    urlsilabus = models.CharField(max_length=5000)
    urlsilabustitle = models.CharField(max_length=5000)

class workshops(models.Model):
    banner = models.CharField(max_length=5000)
    titlebanner = models.CharField(max_length=5000)
    titulo  = models.CharField(max_length=5000)
    ponente = models.CharField(max_length=5000)
    cargo = models.CharField(max_length=5000)
    horas = models.CharField(max_length=5000)
    calificacion = models.CharField(max_length=5000)
    vistas = models.CharField(max_length=5000)
    enlace = models.CharField(max_length=5000)

class pagos(models.Model):
    dni = models.CharField(max_length=5000)
    nombres = models.CharField(max_length=5000)
    apellidos  = models.CharField(max_length=5000)
    correo = models.CharField(max_length=5000)
    celular = models.CharField(max_length=5000)
    curso = models.CharField(max_length=5000)
    medio = models.CharField(max_length=5000)
    voucher = models.CharField(max_length=5000)
    dia = models.CharField(max_length=4)
    mes = models.CharField(max_length=4)
    anio = models.CharField(max_length=4)

class comentarios(models.Model):
    nombre = models.CharField(max_length=5000)
    comentario = models.CharField(max_length=50000)
    dia = models.CharField(max_length=4)
    mes = models.CharField(max_length=4)
    anio = models.CharField(max_length=4)

class postulaciones(models.Model):
    nombres = models.CharField(max_length=5000)
    apellidos  = models.CharField(max_length=5000)
    correo = models.CharField(max_length=5000)
    celular = models.CharField(max_length=5000)
    sitio = models.CharField(max_length=5000)
    comentario = models.CharField(max_length=5000)
    puesto = models.CharField(max_length=5000)
    cv = models.CharField(max_length=5000)
    dia = models.CharField(max_length=4)
    mes = models.CharField(max_length=4)
    anio = models.CharField(max_length=4)

class blogs(models.Model):
    banner = models.CharField(max_length=5000)
    banneralt = models.CharField(max_length=5000)
    titulo = models.CharField(max_length=5000)
    descripcion = models.CharField(max_length=5000)
    fechapublicacion = models.CharField(max_length=5000)
    tiempolectura = models.CharField(max_length=5000)
    url = models.CharField(max_length=5000)
    autor = models.CharField(max_length=5000)
    autoralt = models.CharField(max_length=5000)
    fotoautor = models.CharField(max_length=5000)

class dictar_workshop(models.Model):
    nombres = models.CharField(max_length=5000)
    apellidos = models.CharField(max_length=5000)
    correo = models.CharField(max_length=5000)
    celular = models.CharField(max_length=5000)
    area = models.CharField(max_length=5000)
    otro = models.CharField(max_length=5000)
    cv = models.CharField(max_length=5000)
    dia = models.CharField(max_length=4)
    mes = models.CharField(max_length=4)
    anio = models.CharField(max_length=4)

class dictar_curso(models.Model):
    nombres = models.CharField(max_length=5000)
    apellidos = models.CharField(max_length=5000)
    correo = models.CharField(max_length=5000)
    celular = models.CharField(max_length=5000)
    area = models.CharField(max_length=5000)
    otro = models.CharField(max_length=5000)
    cv = models.CharField(max_length=5000)
    dia = models.CharField(max_length=4)
    mes = models.CharField(max_length=4)
    anio = models.CharField(max_length=4)

class certificados(models.Model):
    codigo = models.CharField(max_length=5000)
    dni = models.CharField(max_length=5000, blank=True, null=True)
    nombres = models.CharField(max_length=5000)
    apellidos = models.CharField(max_length=5000)
    correo = models.CharField(max_length=5000, blank=True, null=True)
    celular = models.CharField(max_length=5000, blank=True, null=True)
    certificado = models.CharField(max_length=5000)
    temaPropuesto = models.CharField(max_length=5000)