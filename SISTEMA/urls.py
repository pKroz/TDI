"""SISTEMA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import Settings
from django.contrib import admin
from django.urls import path
from WEB.TDI.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('workshops/', pWorkshops, name="workshops"),
    path('compra/', pCompra, name="compra"),
    path('nosotros/', pNosotros, name="nosotros"),
    path('trabaja-con-nosotros/', pPostular, name="trabaja-con-nosotros"),
    path('preguntas-frecuentes/', pPreguntas, name="preguntas-frecuentes"),
    path('terminos-y-condiciones/', pTerminos, name="terminos-y-condiciones"),
    path('politicas-de-privacidad/', pPoliticas, name="politicas-de-privacidad"),
    path('dictar-workshop/', pDictarWorkshop, name="dictar-workshop"),
    path('dictar-curso/', pDictarCurso, name="dictar-curso"),
    path('comunidad/', pComunidad, name="comunidad"),
    path('gracias/', pGracias, name="gracias"),
    path('becas/', pBecas, name="becas"),
    #Cursos
    path('cursos/', pCursos, name="cursos"),
    path('cursos/mern/', pMern, name="mern"),
    path('cursos/desarrollo-web/', pDesarrolloWEB, name="desarrollo-web"),
    path('cursos/fundamentos-aws/', pFundamentosAWS, name="fundamentos-aws"),
    #Blogs
    path('blogs/', pBlogs, name="blogs"),
    path('blogs/herramientas-que-todo-desarrollador-web-deberia-conocer-en-el-2021/', pBlog1, name="blog1"),
]
