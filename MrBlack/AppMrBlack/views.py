from threading import local
from django.http import HttpResponse
from django.shortcuts import render
from .models import Hamburguesas, Locales
from .forms import HamburguesaFormulario, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            psw = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=psw)

            if user is not None:
                login(request,user)
                
                return render(request, 'inicio.html', {"mensaje":f"Bienvenidx {usuario}"} )
            else:
                return render(request, 'inicio.html', {"mensaje":"Error, los datos ingresados son incorrectos"} )
        else:
                return render(request, 'inicio.html', {"mensaje":"Error, formulario incorrecto"} )
    form = AuthenticationForm()

    return render(request, 'login.html',{'form':form})

def register(request):
    if request.method =="POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request, 'inicio.html',{'mensaje':'Usuario creado con éxito'})
        
    else: 
        form = UserRegisterForm()
    return render(request, 'registro.html', {'form':form})