from django.db import models
from django.contrib.auth.models import User


class Telefono(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=30)

    class Meta:
        verbose_name='Telefonos'
        verbose_name_plural='Telefonos Registrados'

    def __str__(self):
        return self.numero