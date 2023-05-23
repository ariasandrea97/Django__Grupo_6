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
    
 
    path('registro/', views.registro, name="registro"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),


    path('listar_reservas/', views.listar_reservas, name="listar_reservas"),
    path('enviar_consulta',views.enviar_consulta, name="enviar_consulta"),
    path('mi_cuenta/', views.mi_cuenta, name="mi_cuenta"),

    path('enviar_reserva_hotel',views.enviar_reserva_hotel, name="enviar_reserva_hotel"),
    path('detalle_hotel_Mendoza',views.detalle_hotel_Mendoza, name="detalle_hotel_Mendoza"),
    path('detalle_hotel_PuestaSol',views.detalle_hotel_PuestaSol, name="detalle_hotel_PuestaSol"),
    path('detalle_hotel_Algodon',views.detalle_hotel_Algodon, name="detalle_hotel_Algodon"),


]