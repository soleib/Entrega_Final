from django.urls import path
from AppMrBlack import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('locales/',views.locales, name="Locales"),
    path('hamburguesas/',views.hamburguesas, name="Hamburguesas"),
    path('panchos/',views.panchos, name="Panchos"),
    path('HamburguesaFormulario/', views.hamburguesaFormulario, name="HamburguesaFormulario"),
    path('busquedaLocal/', views.busquedalocal, name="BusquedaLocal"),
    path('buscar/', views.buscar),

    #CRUD
    path('leerhamburguesas/',views.leerHamburguesas,name="leerhamburguesas"),
    path('eliminarHamburguesa/<id>',views.eliminar_hamburguesa,name="EliminarHamburguesa"),
    path('editarHamburguesa<id>',views.editar_hamburguesa,name="EditarHamburguesa"),

    #VISTAS BASADAS EN CLASES
    path('hamburguesas/list',views.HamburguesaList.as_view(),name='List'),
    path('hamburguesas/detail<pk>',views.HamburguesaDetalle.as_view(),name='Detail'),
    path('hamburguesas/edit<pk>',views.HamburguesaUpdate.as_view(),name='Edit'),
    path('hamburguesas/delete<pk>',views.HamburguesaoDelete.as_view(),name='Delete'),
    path('hamburguesas/create',views.HamburguesaCreacion.as_view(),name='New'),

    path('local/list',views.LocalList.as_view(),name='ListLocal'),
    path('local/detail<pk>',views.LocalDetalle.as_view(),name='DetailLocal'),
    path('local/edit<pk>',views.LocalUpdate.as_view(),name='EditLocal'),
    path('local/delete<pk>',views.LocalDelete.as_view(),name='DeleteLocal'),
    path('local/create',views.LocalCreacion.as_view(),name='NewLocal'),    

    #Iniciar sesión, Registrar, Logout, Editar Perfil
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editarPerfil',views.editarPerfil, name="EditarPerfil"),

    #inicio
    path('busquedaHamburguesa/', views.busquedaHamburguesa, name="BusquedaHamburguesa"),
    path('buscarHamburguesa/',views.buscarHamburguesa)]
