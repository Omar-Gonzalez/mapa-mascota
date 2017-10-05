from django.shortcuts import render
from straymap.forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'app.html')
    else:
        return render(request, 'app.html')
