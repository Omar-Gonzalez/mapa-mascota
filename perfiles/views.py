from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


def perfil(request, user_id):
    if user_id is not None and request.user.is_authenticated():
        return render(request, "perfiles/perfil.html", {
            'query_user_id': user_id
        })

    registroForm = CustomUserCreationForm()
    loginForm = AuthenticationForm()

    if request.method == "POST":
        if "login-form" in request.POST:
            loginForm = AuthenticationForm(data=request.POST)
            if loginForm.is_valid():
                username = loginForm.cleaned_data.get("username")
                raw_password = loginForm.cleaned_data.get("password")
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')

        if "registro-form" in request.POST:
            registroForm = CustomUserCreationForm(request.POST)
            if registroForm.is_valid():
                registroForm.save()
                username = registroForm.cleaned_data.get("username")
                raw_password = registroForm.cleaned_data.get("password1")
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')

    return render(request, "perfiles/perfil.html", {
        'registroForm': registroForm,
        'loginForm': loginForm
    })


def usuario(request, user_id):
    perfil = {}
    if str(user_id) == "propio":
        perfil = User.objects.filter(id=request.user.id).first()
    else:
        perfil = User.objects.filter(id=int(user_id)).first()
    return render(request, "includes/usuario.html", {
        'perfil': perfil
    })
