from django.shortcuts import render
from .models import Mascota


def feed(request):
    mascotas = Mascota.objects.all().order_by('-id')[:50]
    return render(request, 'app.html', {
            'mascotas': mascotas
        })
