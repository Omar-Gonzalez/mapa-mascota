from django.contrib import admin
from .models import Avistamiento


class AvistamientoAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'mascota',
        'lat',
        'lng',
        'direccion',
        'observaciones',
        'creado',
        'actualizado'
    ]


admin.site.register(Avistamiento, AvistamientoAdmin)
