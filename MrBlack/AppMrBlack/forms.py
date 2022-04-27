

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class HamburguesaFormulario(forms.Form):

    nombrehamburguesa = forms.CharField()
    tipopan = forms.CharField()
    tipocarne = forms.CharField()
    cantidadmedallones = forms.IntegerField()
    aderezo = forms.CharField()
<<<<<<< HEAD
    salsaMrBlack = forms.CharField()
    fechacreacion = forms.DateField()
=======
    salsaMrBlack = forms.BooleanField()
    fechacreacion = forms.DateField()


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1= forms.CharField(label='Introduzca la contraseña',widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita la contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']

        help_texts ={k:"" for k in fields} 
>>>>>>> 8899c130c9ae94fa21e1a29a8e9d302e1ba76e9d
