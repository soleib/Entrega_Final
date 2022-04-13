from django.urls import path
from AppMrBlack import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('locales/',views.locales, name="Locales"),
    path('hamburguesas/',views.hamburguesas, name="Hamburguesas"),
    path('panchos/',views.panchos, name="Panchos"),
    path('HamburguesaFormulario/', views.hamburguesaFormulario, name="HamburguesaFormulario"),
    path('busquedaLocal/', views.busquedalocal, name="BusquedaLocal"),
    path('buscar/', views.buscar),
  
]