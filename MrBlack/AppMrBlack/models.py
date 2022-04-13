from django.db import models

# Create your models here.
class Locales(models.Model):
    nombrelocal = models.CharField('nombrelocal',max_length=45)
    ciudad = models.CharField('ciudad',max_length=45)
    provincia = models.CharField('provincia',max_length=45)
    direccion = models.CharField('direccion',max_length=45)
    altura = models.IntegerField()
    fechaapertura = models.DateField('fechaapertura')

    def __str__(self):
        return f'{self.nombrelocal} - Ubicación: {self.direccion} {self.altura} - {self.ciudad} {self.provincia}'

class Hamburguesas(models.Model):
    nombrehamburguesa = models.CharField('nombrehamburguesa',max_length=45)
    tipopan = models.CharField('tipopan',max_length=45)
    tipocarne = models.CharField('tipocarne',max_length=45)
    cantidadmedallones = models.IntegerField()
    aderezo = models.CharField('aderezo',max_length=45)
    salsaMrBlack = models.BooleanField()
    fechacreacion = models.DateField('fechacreacion')

    def __str__(self):
        return f'{self.nombrehamburguesa}'

class Panchos(models.Model):
    nombrepancho = models.CharField('nombrepancho',max_length=45)
    tamaño = models.CharField('tipopan',max_length=45)
    aderezo = models.CharField('aderezo',max_length=45)
    salsa = models.CharField('salsa',max_length=45)
    fechacreacion = models.DateField('fechacreacion')

    def __str__(self):
        return f'{self.nombrepancho}'
    