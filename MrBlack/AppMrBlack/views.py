from threading import local
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from .models import Avatar, Hamburguesas, Locales
from .forms import HamburguesaFormulario   

from .models import Hamburguesas, Locales
from .forms import HamburguesaFormulario, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def inicio(request):
    #avatar= Avatar.objects.get(user=request.user.id)
    return render(request, 'inicio.html')

def hamburguesas(request):
   # avatar= Avatar.objects.get(user=request.user.id)
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


def leerHamburguesas(request):
    hamburguesa= Hamburguesas.objects.all()
    contexto={"lista_hamburguesa":hamburguesa}
    return render(request,'leerhamburguesas.html',contexto)


def eliminar_hamburguesa(request,id):
    hamburguesa=Hamburguesas.objects.get(id=id)
    hamburguesa.delete()

    hamburguesa= Hamburguesas.objects.all()
    contexto={"lista_hamburguesa":hamburguesa}
    return render(request,'leerhamburguesas.html',contexto)

def editar_hamburguesa(request,id):
    hamburguesa=Hamburguesas.objects.get(id=id)

    if request.method == "POST":
        miFormulario=HamburguesaFormulario(request.POST)

        if miFormulario.is_valid():
            imformacion=miFormulario.cleaned_data

            hamburguesa.nombrehamburguesa=imformacion['nombrehamburguesa']
            hamburguesa.tipopan=imformacion['tipopan']
            hamburguesa.tipocarne=imformacion['tipocarne']
            hamburguesa.cantidadmedallones=imformacion['cantidadmedallones']
            hamburguesa.aderezo=imformacion['aderezo']
            hamburguesa.salsaMrBlack=imformacion['salsaMrBlack']
            hamburguesa.fechacreacion=imformacion['fechacreacion']

            hamburguesa.save()

            return render(request,'inicio.html')

    else:
        miFormulario=HamburguesaFormulario(
            initial={
                'nombrehamburguesa':hamburguesa.nombrehamburguesa,
                'tipopan':hamburguesa.tipopan,
                'tipocarne':hamburguesa.tipocarne,
                'cantidadmedallones':hamburguesa.cantidadmedallones,
                'aderezo':hamburguesa.aderezo,
                'salsaMrBlack':hamburguesa.salsaMrBlack,
                'fechacreacion':hamburguesa.fechacreacion})

    return render(request,'editarHamburguesa.html',{"miFormulario":miFormulario,"hamburguesa_nombre":hamburguesa.nombrehamburguesa})


class HamburguesaList(ListView):

      
      model = Hamburguesas
      template_name = "hamburguesas_list.html"
   



class HamburguesaDetalle(DetailView):

      model = Hamburguesas
      template_name = "hamburguesas_detalle.html"



class HamburguesaCreacion(CreateView):

      model = Hamburguesas
      template_name="hamburguesas_form.html"
      success_url = "/hamburguesas/list"
      fields = ['nombrehamburguesa','tipopan','tipocarne','cantidadmedallones','aderezo','salsaMrBlack','fechacreacion']


class HamburguesaUpdate(UpdateView):

      model = Hamburguesas
      template_name="hamburguesas_form.html"
      success_url = "/AppMrBlack/hamburguesas/list"
      fields  = ['nombrehamburguesa','tipopan','tipocarne','cantidadmedallones','aderezo','salsaMrBlack','fechacreacion']


class HamburguesaoDelete(DeleteView):

      model = Hamburguesas
      template_name="hamburguesas_confirm_delete.html"
      success_url = "/AppMrBlack/hamburguesas/list"

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

