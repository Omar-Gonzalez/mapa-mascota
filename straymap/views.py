from django.shortcuts import render
from .forms import RegisterForm


def home(request):
    registerForm = RegisterForm()
    return render(request, 'app.html', {
            'registerForm': registerForm
        })
