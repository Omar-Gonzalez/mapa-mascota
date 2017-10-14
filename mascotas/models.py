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


class Raza(models.Model):
    raza = models.CharField(max_length=50)

    def save(self, force_insert=False, force_update=False):
        self.raza = self.raza.upper()
        super(Raza, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas de mascotas"

    def __str__(self):
        return self.raza


class Tamaño(models.Model):
    tamaño = models.CharField(max_length=50)

    def save(self, force_insert=False, force_update=False):
        self.tamaño = self.tamaño.upper()
        super(Tamaño, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Tamño"
        verbose_name_plural = "Tamaños de mascotas"

    def __str__(self):
        return self.tamaño


class Mascota(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie)
    raza = models.ForeignKey(Raza)
    tamaño = models.ForeignKey(Tamaño)
    genero = models.ForeignKey(Genero)
    color = models.ForeignKey(Color)
    nombre = models.CharField(max_length=50)
    edad_años = models.IntegerField()
    señas = models.TextField(null=True, blank=True, default="")
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Mascotas"
        verbose_name_plural = "Feed de Mascotas"

    def __str__(self):
        return self.user.username
