from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Telefono


class CustomUserCreationForm(UserCreationForm):
    telefono = forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'telefono')

    def save(self):
        new_user = super(CustomUserCreationForm, self).save(commit=False)
        new_user.save()
        # guarda numero de telefono
        if len(self.cleaned_data['telefono']) > 1:
            telefono = Telefono()
            telefono.user = new_user
            telefono.numero = self.cleaned_data['telefono']
            telefono.save()
        return new_user
