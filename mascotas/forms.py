from django.forms import ModelForm
from .models import Mascota


class MascotaForm(ModelForm):

    class Meta():
        model = Mascota
        exclude = ['creado','user']