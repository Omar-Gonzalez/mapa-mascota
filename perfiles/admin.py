from django.contrib import admin
from .models import Telefono


class TelefonoAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "numero"
    ]


admin.site.register(Telefono, TelefonoAdmin)
