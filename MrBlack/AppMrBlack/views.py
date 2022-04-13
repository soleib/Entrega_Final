from threading import local
from django.http import HttpResponse
from django.shortcuts import render
from .models import Hamburguesas, Locales
from .forms import HamburguesaFormulario   

# Create your views here.
def inicio(request):
    
    return render(request, 'inicio.html')

def hamburguesas(request):
    
    return render(request, 'hamburguesas.html')

def panchos(request):
    
    return render(request, 'panchos.html')

def locales(request):
    
    return render(request, 'locales.html')

def agregalocal(request, nombrelocal, ciudad, provincia, direccion, altura, fechaapertura):

    tienda = Locales(nombrelocal=nombrelocal, ciudad=ciudad, provincia=provincia, direccion=direccion,altura=altura, fechaapertura=fechaapertura)
    tienda.save()
    return render(request, 'agregafamiliar.html', {'nombrelocal': nombrelocal,'ciudad': ciudad, 'provincia': provincia,'direccion': direccion, 'altura': altura, 'fechaapertura': fechaapertura})


def hamburguesaFormulario(request):
    if request.method == "POST":
        miFormulario = HamburguesaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            hamburguesa = Hamburguesas(nombrehamburguesa = informacion['nombrehamburguesa'], tipopan = informacion['tipopan'], tipocarne = informacion['tipocarne'], cantidadmedallones = informacion['cantidadmedallones'], aderezo = informacion['aderezo'], salsaMrBlack = informacion["salsaMrBlack"], fechacreacion = informacion['fechacreacion'])
            hamburguesa.save()
            return render(request, "inicio.html")
    else:
        miFormulario = HamburguesaFormulario()
        return render(request, 'HamburguesaFormulario.html', {'miFormulario':miFormulario})

def busquedalocal(request):
    return render(request, "busquedaLocal.html")

def buscar(request):
    if request.GET["nombrelocal"]:
        nombrelocal = request.GET["nombrelocal"]
        locales = Locales.objects.filter(nombrelocal = nombrelocal)

        return render(request, "resultadoBusqueda.html", {"locales":locales,"nombrelocal" : nombrelocal })
    else:
        return HttpResponse("No enviaste Datos")

