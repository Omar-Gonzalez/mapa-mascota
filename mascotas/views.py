from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Mascota
from .forms import MascotaForm


def home(request):
    return render(request, 'home.html')


def feed(request):
    mascotas = Mascota.objects.all().order_by('-id')[:50]
    return render(request, 'widgets/feed.html', {
        'mascotas': mascotas
    })


def test(request):
    return render(request, 'test.html')


def reporta_mascota(request):
    form = MascotaForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'forms/reporta-mascota.html', {
        'form': form
    })
