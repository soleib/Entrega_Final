

from dataclasses import field
import email
from tkinter import image_names
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class HamburguesaFormulario(forms.Form):

    nombrehamburguesa = forms.CharField()
    tipopan = forms.CharField()
    tipocarne = forms.CharField()
    cantidadmedallones = forms.IntegerField()
    aderezo = forms.CharField()

    salsaMrBlack = forms.CharField()
    fechacreacion = forms.DateField()


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1= forms.CharField(label='Introduzca la contraseña',widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita la contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']

        help_texts ={k:"" for k in fields} 

class UserEditForm(UserCreationForm):
    #Acá se definen las opciones que queres editar del usuario.
    #imagen=
    nombre = forms.CharField()
    descripcion = forms.CharField()
    web = forms.URLField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Introduzca la contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['nombre','descripcion','web','email','password1','password2']
        #fields = ['descripcion','web','email','password1','password2']
        help_texts= {k:"" for k in fields}

