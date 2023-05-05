from django.urls import path, re_path
from . import views

#from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView




urlpatterns = [
    path('', views.index, name="index"),

    path('nosotros/', views.nosotros, name="nosotros"),
    path('alojamiento/', views.alojamiento, name="alojamiento"),
    path('gastronomia/', views.gastronomia, name="gastronomia"),
    path('circuito_turistico/', views.circuito_turistico, name="circuito_turistico"),
    path('ruta_del_vino/', views.ruta_del_vino, name="ruta_del_vino"),
    
    path('enviar_consulta',views.enviar_consulta, name="enviar_consulta"),

    path('registro/', views.registro, name="registro"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),

    path('mis_reservas/', views.mis_reservas, name="mis_reservas"),


]