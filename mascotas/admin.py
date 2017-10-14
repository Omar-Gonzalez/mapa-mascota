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


class MascotaAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "especie",
        "genero",
        "color",
        "nombre",
        "edad",
        "señas"
    ]


admin.site.register(Mascota, MascotaAdmin)