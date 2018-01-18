from django.db import models
from mascotas.models import Mascota
from django.contrib.auth.models import User


class Avistamiento(models.Model):
    user = models.ForeignKey(User)
    mascota = models.ForeignKey(Mascota)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.TextField()
    observaciones = models.TextField(null=True, blank=True)
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)
