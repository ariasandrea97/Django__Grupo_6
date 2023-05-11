from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

#
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages



#Definicion de los formularios:
from .forms import EnviarConsultaForm



def index(request):
    # Hagamos de cuenta que este dato viene de la BBDD

    # usuario = {
    #     'nombre': 'Maria',
    #     'apellido': 'Del Cerro',
    #     'mail': 'maria@delcerro',
    #     'valid': False
    # }

    # listado_usuarios = [
    #     {
    #         'name': 'Maria',
    #         'last_name': 'Del Cerro',
    #         'age': 25,
    #         'valid': False,
    #     },
    #     {
    #         'name': 'Florencia',
    #         'last_name': 'Perez',
    #         'age': 30,
    #         'valid': False,
    #     },
    #     {
    #         'name': 'Martin',
    #         'last_name': 'Del Moro',
    #         'age': 35,
    #         'valid': False,
    #     },
    # ]

    context = {
        # 'first_name': 'Carlos',
        # 'last_name': 'Lopez',
     #   'usuario': usuario,
        #'usuario': usuario_ficticio,
      #  'listado_usuarios': listado_usuarios
    }

    return render(request, 'Viajeros/index.html', context)




def baja_persona(request):
    context={}
    return render(request, 'Viajeros/baja_persona.html', context)

def nosotros(request):
    context={}
    return render(request, 'Viajeros/paginas/nosotros.html', context)

def alojamiento(request):
    context={}
    return render(request, 'Viajeros/paginas/alojamiento.html', context)

def gastronomia(request):
    context={}
    return render(request, 'Viajeros/paginas/gastronomia.html', context)

def circuito_turistico(request):
    context={}
    return render(request, 'Viajeros/paginas/circuito_turistico.html', context)


def ruta_del_vino(request):
    context={}
    return render(request, 'Viajeros/paginas/ruta_del_vino.html', context)



def enviar_consulta(request):
    if request.method == "POST":
        form = EnviarConsultaForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")
            context= {  }
            return render(request, 'Viajeros/index.html', context)

    else:
        # GET
        form = EnviarConsultaForm()

    context = {'form': form}
    return render(request, 'Viajeros/paginas/enviar_consulta.html', context)



def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()  #guardamos el usuario
            # nombre_usuario = form.cleaned_data.get('username')
            # messages.success(request, f"Nueva Cuenta creada : {nombre_usuario}")
            messages.add_message(request, messages.SUCCESS, 'Usuario dado de alta: ' + form.cleaned_data.get('username'), extra_tags="tag1")

            login(request,usuario)
            messages.add_message(request, messages.SUCCESS, 'Ha iniciado sesion como: ' + form.cleaned_data.get('username'), extra_tags="tag1")
            return render(request, 'Viajeros/index.html')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form =UserCreationForm      
    return render(request, 'Viajeros/usuario/registro.html',{"form": form}) 

##
def logout_request(request):
    logout(request)
    messages.info(request,"Sesion finalizada")
    return render(request, 'Viajeros/index.html') 

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            usuario =form.cleaned_data.get('username')
            contraseña= form.cleaned_data.get('password')
            user= authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request,user)
                messages.info(request, f"Ha iniciado sesion como: {usuario}")
                return render(request, 'Viajeros/index.html')

    form = AuthenticationForm()
    return render(request, 'Viajeros/usuario/login.html',{"form": form}) 

##

def mis_reservas(request):

    context={}
    return render(request, 'Viajeros/paginas/mis_reservas.html', context)