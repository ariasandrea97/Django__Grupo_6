from django import forms
from django.core.exceptions import ValidationError

#
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



BIRTH_YEAR_CHOICES = range(1980,2006)
TYPE_CHOICES = [
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
]

TYPE_CHOICES2 = [
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
]

TYPE_RESERVA = [
    ("Alojamiento", "Alojamiento"),
    ("Excursion", "Excursion"),
    ("Otros", "Otros"),
]

class AltaPersonaForm(forms.Form):
  #  nombre = forms.CharField(label="Nombre ",widget=forms.TextInput(attrs={'class': 'nombre_alumno rojo'}), required=True)
    nombre = forms.CharField(label="Nombre ",widget=forms.TextInput(), required=True)
    apellido = forms.CharField(label="Apellido ", required=True)
    mail = forms.EmailField(label="Mail", required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    # contraseña = forms.CharField(label="Password", required=True)
    #contraseña2 = forms.PasswordInput(label="Confirme Password")
    #validar contraseña
    def clean_mail(self):
    # Validación del campo Mail

        data = self.cleaned_data["mail"]
        # if True:
        #     raise ValidationError("El mail utilizado ya existe")

        return data

class EnviarConsultaForm(forms.Form):
        nombre = forms.CharField(label="Nombre ",widget=forms.TextInput(), required=True)
        apellido = forms.CharField(label="Apellido ", required=True)
        mail = forms.EmailField(label="Mail", required=True)
        telefono = forms.CharField(label="Telefono", required=True)


        # fecha_ingreso = forms.DateField(
        #     widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
        # )
        tipo = forms.ChoiceField(
            label="Tipo de reserva",
            widget=forms.Select,
            choices=TYPE_RESERVA,
        )
        # Campo Fecha con date picker en el chrome.
        fecha_desde = forms.DateField(label="Fecha Desde", widget=forms.DateInput(attrs={'type': 'date'}))
        fecha_hasta = forms.DateField(label="Fecha Hasta", widget=forms.DateInput(attrs={'type': 'date'}))
        #validar que la fecha hasta sea mayor que la fecha desde

        adultos = forms.ChoiceField(
            label="Adultos",
            widget=forms.Select,
            choices=TYPE_CHOICES,
        )
        niños  = forms.ChoiceField(
            label="Niños",
            widget=forms.Select,
            choices=TYPE_CHOICES2,
        )

        mensaje = forms.CharField(widget=forms.Textarea)
        
        def clean_mail(self):
            # Validación del campo Mail

            # Para mas detalle
            # https://docs.djangoproject.com/en/4.2/ref/forms/validation/

            # aqui podemos poner la logica de negocio necesaria para 
            # efectivamente validar si por ejemplo el campo mail es valido
            # o no.

            # Si es valido se devuelve la info, caso contrario se lanza 
            # un ValidationError.

            # Pueden cambiar la logica del if para probar ambos casos.

            data = self.cleaned_data["mail"]
        # if True:
        #     raise ValidationError("El mail utilizado ya existe")

            # Always return a value to use as the new cleaned data, even if
            # this method didn't change it.
            return data



class InicioSesionForm(forms.Form):
    mail = forms.EmailField(label="Mail", required=True)
    # contraseña = forms.CharField(label="Password", required=True)
    contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean_mail(self):
    # Validación del campo Mail

        data = self.cleaned_data["mail"]
        # if True:
        #     raise ValidationError("El mail utilizado ya existe")

        return data





