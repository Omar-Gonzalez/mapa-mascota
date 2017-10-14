from django.db import models
from django.contrib.auth.models import User


class Especie(models.Model):
    especie = models.CharField(max_length=50)

    def save(self, force_insert=False, force_update=False):
        self.especie = self.especie.upper()
        super(Especie, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies de mascotas"

    def __str__(self):
        return self.especie


class Genero(models.Model):
    genero = models.CharField(max_length=50)

    def save(self, force_insert=False, force_update=False):
        self.genero = self.genero.upper()
        super(Genero, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos de mascotas"

    def __str__(self):
        return self.genero


class Color(models.Model):
    color = models.CharField(max_length=50)

    def save(self, force_insert=False, force_update=False):
        self.color = self.color.upper()
        super(Color, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colores de mascotas"

    def __str__(self):
        return self.color


class Mascota(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie)
    genero = models.ForeignKey(Genero)
    color = models.ForeignKey(Color)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    señas = models.TextField(null=True, blank=True, default="")

    class Meta:
        verbose_name = "Mascotas"
        verbose_name_plural = "Feed de Mascotas"

    def __str__(self):
        return self.user.username
