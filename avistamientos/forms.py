from django.forms import ModelForm
from .models import Avistamiento


class AvistamientoForm(ModelForm):
    class Meta:
        model = Avistamiento
        exclude = ["creaado", "actualizado"]
