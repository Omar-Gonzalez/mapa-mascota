from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect


def registro(request):
    registroForm = CustomUserCreationForm(request.POST)
    if registroForm.is_valid():
        registroForm.save()
        username = registroForm.cleaned_data.get("username")
        raw_password = registroForm.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('home')
    return render(request, "registration/registro.html", {
        "registroForm": registroForm
    })


def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
