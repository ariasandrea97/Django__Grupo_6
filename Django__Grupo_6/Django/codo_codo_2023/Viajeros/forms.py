from django import forms
from django.core.exceptions import ValidationError
from .models import Reservas, Hotel, Servicios


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


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


class EnviarReservaForm(forms.ModelForm):
    fecha_desde = forms.DateField(label="Fecha Desde", widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_hasta = forms.DateField(label="Fecha Hasta", widget=forms.DateInput(attrs={'type': 'date'}))
    Tipo_reserva= "Excursion"

    # hotel=forms.ModelChoiceField(queryset=Hotel.objects.order_by('id').values_list('nombre_hotel'))
    # excursion=forms.ModelChoiceField(queryset=Excursion.objects.order_by('id').values_list('nombre_excursion'))

    class Meta:
        model = Reservas
        fields= [ 'fecha_desde', 'fecha_hasta', 'adulto','menor']
    
    def clean(self):
        cleaned_data = super().clean()
        fechaD = cleaned_data.get("fecha_desde")
        fechaH = cleaned_data.get("fecha_hasta")

        # print(cleaned_data)
        if fechaD is not None and fechaH is not None and fechaD > fechaH:
            raise ValidationError("La Fecha Hasta debe ser posterior a la Fecha Desde")
        
        return cleaned_data

###########################################################################
class EnviarReservaHotelForm(forms.ModelForm):  # para reserva de Hotel
    fecha_desde = forms.DateField(label="Fecha Desde", widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_hasta = forms.DateField(label="Fecha Hasta", widget=forms.DateInput(attrs={'type': 'date'}))
    # Tipo_reserva = forms.CharField('Tipo de reserva', value='Alojamiento')
    # hotel=forms.ModelChoiceField(queryset=Hotel.objects.order_by('id').values_list('nombre_hotel'))
    # excursion=forms.ModelChoiceField(queryset=Excursion.objects.order_by('id').values_list('nombre_excursion'))

    
    hotel=forms.ModelChoiceField(queryset=Hotel.objects.order_by('nombre_hotel'))

    def clean(self):
        cleaned_data = super().clean()
        fechaD = cleaned_data.get("fecha_desde")
        fechaH = cleaned_data.get("fecha_hasta")

        # print(cleaned_data)
        if fechaD is not None and fechaH is not None and fechaD > fechaH:
            raise ValidationError("La Fecha Hasta debe ser posterior a la Fecha Desde")
    # return cleaned_data
        
    def clean_hotel(self):
        hotel = self.cleaned_data['hotel']
        print("hotel:", hotel)
        return hotel

    class Meta:
        model = Reservas

        fields= [ 'fecha_desde', 'fecha_hasta', 'adulto','menor', 'hotel']

        
     

######################################################################

class AltaUsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields =  ['first_name', 'last_name', 'email', 'username','password1', 'password2']

    # Check unique email
    # Email exists && account active -> email_already_registered
    # Email exists && account not active -> delete previous account and register new one
    def clean_email(self):
        email_passed = self.cleaned_data.get("email")
        email_already_registered = User.objects.filter(email = email_passed).exists()
        user_is_active = User.objects.filter(email = email_passed, is_active = 1)
        if email_already_registered and user_is_active:
            print('email_already_registered and user_is_active')
            raise forms.ValidationError("Email already registered.")
        elif email_already_registered:
            print('email_already_registered')
            User.objects.filter(email = email_passed).delete()

        return email_passed