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
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
  
]