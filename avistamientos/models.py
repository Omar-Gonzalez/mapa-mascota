from django.db import models
from mascotas.models import Mascota
from django.contrib.auth.models import User


class Avistamiento(models.Model):
    user = models.ForeignKey(User)
    mascota = models.ForeignKey(Mascota)
