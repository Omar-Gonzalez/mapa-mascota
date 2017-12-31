from django.forms import ModelForm
from .models import Mascota


class MascotaForm(ModelForm):

    class Meta():
        model = Mascota
        exclude = ['creado', 'user']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(MascotaForm, self).__init__(*args, **kwargs)

    def save(self):
        mascota = super(MascotaForm, self).save(commit=False)
        mascota.user = self.user
        mascota.save()
        return mascota
