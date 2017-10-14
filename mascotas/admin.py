from django.contrib import admin
from .models import *


class EspecieAdmin(admin.ModelAdmin):
    list_display = [
        "especie"
    ]


admin.site.register(Especie, EspecieAdmin)


class GeneroAdmin(admin.ModelAdmin):
    list_display = [
        "genero"
    ]


admin.site.register(Genero, GeneroAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = [
        "color"
    ]


admin.site.register(Color, ColorAdmin)


class RazaAdmin(admin.ModelAdmin):
    list_display = [
        "raza"
    ]


admin.site.register(Raza, RazaAdmin)


class TamañoAdmin(admin.ModelAdmin):
    list_display = [
        "tamaño"
    ]


admin.site.register(Tamaño, TamañoAdmin)


class MascotaAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "especie",
        "raza",
        "genero",
        "color",
        "nombre",
        "edad_años",
        "señas",
        "creado"
    ]


admin.site.register(Mascota, MascotaAdmin)