
from django import forms
from django import *
from .models import pagos
from .models import cursos
from django.db import models

class compraForm(forms.Form):
    class Meta:
        model = pagos
        fields = ['dni','nombres','apellidos','correo','celular','curso','medio','voucher']

    dni = forms.CharField(label='DNI', required= True, max_length=200, min_length=8, widget=forms.TextInput(attrs={
      'class': 'form-control',
       'placeholder' : 'Ingresar DNI'}))
    nombres = forms.CharField(label='Nombres', required= True, max_length=200, widget=forms.TextInput(attrs={
      'class': 'form-control',
       'placeholder' : 'Ingresar nombres'}))
    apellidos = forms.CharField(label='Apellidos', max_length=200, widget=forms.TextInput(attrs={
      'class': 'form-control',
       'placeholder' : 'Ingresar apellidos'}))
    correo = forms.EmailField(label='Correo', max_length=200, widget=forms.TextInput(attrs={
      'class': 'form-control',
       'placeholder' : 'Ingresar email'}))
    celular = forms.CharField(label='Celular', max_length=200, widget=forms.TextInput(attrs={
      'class': 'form-control',
       'placeholder' : 'Ingresar celular'}))
    curso = forms.ModelChoiceField(label='Cursos', queryset=cursos.objects.all())
    medio = forms.CharField(label='Name', max_length=200, widget=forms.TextInput(attrs={
      'class': 'form-control',
       'placeholder' : 'Ingresar tu nombre'}))
    voucher = forms.ImageField(label="voucher")