from django.db import models


# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



# class Usuario(models.Model):
#     # username = None
#     # # email = models.EmailField('email', unique=True)
#     # nombre = models.CharField(max_length=50)
#     # apellido = models.CharField(max_length=50)
# #     is_staff = models.BooleanField(default=False)
#     pass

#     #USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['nombre', 'apellido', 'username']
    
#     def get_full_name(self):
#         full_name = '%s %s' % (self.nombre, self.apellido)
#         return full_name.strip()

#     def get_short_name(self):
#         return self.nombre
    


class Hotel(models.Model):
    nombre_hotel = models.CharField(max_length=128, verbose_name="Hotel")
    direccion = models.CharField(max_length=128, verbose_name="Direccion")
    categoria = models.IntegerField(verbose_name="Categoria")
    
    def __str__(self):
	    return self.nombre_hotel

class Servicios(models.Model):
    servicio = models.CharField(max_length=128)
    hotel = models.ManyToManyField(Hotel)
    
    def __str__(self):
	    return self.servicio


# class Tipo_reserva(models.Model):
#     nombre_reserva = models.CharField(max_length=50, unique=True)

#     def __str__(self):
# 	    return self.nombre_reserva

class Reservas(models.Model):
    TIPO_CHOICES = (
        ('Alojamiento', 'Alojamiento'),
        ('Excursion', 'Excursion'),
        ('Gastronomia', 'Gastronomia'),
    )
    # TIPO_HOTEL = (
    #     ('1', 'Hotel Mendoza'),
    #     ('2', 'Puesta del Sol'),
    #     ('3', 'Hotel Algodon Wine States'),
    # )
    TIPO_EXCURSION = (
        ('1', 'Cañon del Atuel'),
        ('2', 'Villavicencio'),
        ('3', 'Bodegas y Viñedos'),
    )

    TIPO_ADULTO = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    )

    TIPO_MENOR = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    )

    fecha_registracion= models.DateField(null=True)
    fecha_desde = models.DateField(null=True)
    fecha_hasta = models.DateField(null=True)
    usuario = models.CharField(max_length=128, verbose_name="usuario ")
    #usuario = models.ForeignKey(User, null=True, blank= True, on_delete=models.CASCADE)
    Tipo_reserva = models.CharField('Tipo de reserva', max_length=15, choices=TIPO_CHOICES, default='Alojamiento')
   

    adulto = models.CharField('Cantidad de Adultos', max_length=2, choices=TIPO_ADULTO, default='1')
    menor= models.CharField('Cantidad de Menores', max_length=2, choices=TIPO_MENOR, default='0')
    estado = models.BooleanField(default=True)  
    #hotel = models.ManyToManyField(Hotel)#, choices=TIPO_HOTEL) # Muchos a muchos
    # hotel = models.CharField(max_length=150, default=' ')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=' ') # muchos a uno


    def __str__(self):
	    return self.hotel
 
