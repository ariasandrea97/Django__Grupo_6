from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone



class Usuario(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mail =models.EmailField(max_length=128)

    def __str__(self):
	    return self.mail

