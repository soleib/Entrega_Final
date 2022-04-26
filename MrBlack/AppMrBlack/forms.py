from django import forms

class HamburguesaFormulario(forms.Form):

    nombrehamburguesa = forms.CharField()
    tipopan = forms.CharField()
    tipocarne = forms.CharField()
    cantidadmedallones = forms.IntegerField()
    aderezo = forms.CharField()
    salsaMrBlack = forms.CharField()
    fechacreacion = forms.DateField()