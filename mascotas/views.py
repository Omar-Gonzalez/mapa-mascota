from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'mascotas/home.html')


def feed(request, user_id, mascota_id):
    if user_id is not None:
        query_user = User.objects.filter(id=user_id).first()
        mascotas = Mascota.objects.filter(
            user=user_id).all().order_by('-id')[:50]
        return render(request, 'mascotas/feed.html', {
            'mascotas': mascotas,
            'user_feed_name': query_user.username
        })

    if mascota_id is not None:
        mascota = Mascota.objects.filter(id=mascota_id).first()
        return render(request, 'mascotas/mascota-detalle.html', {
            'mascota': mascota
        })

    mascotas = Mascota.objects.all().order_by('-id')[:50]
    return render(request, 'mascotas/feed.html', {
        'mascotas': mascotas
    })


def reporta_mascota(request):
    form = MascotaForm(request.user)
    if request.method == "POST":
        form = MascotaForm(request.user, request.POST)
        if form.is_valid() and request.user.is_authenticated():
            form.save()
            return redirect('home')
        else:
            # return redirect with errors
            return redirect('home')
    return render(request, 'mascotas/reporta-mascota.html', {
        'form': form
    })
