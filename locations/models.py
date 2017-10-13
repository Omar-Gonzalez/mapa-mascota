from django.db import models
from django.contrib.auth.models import User

class Especie(models.Model):
    nombre = models.CharField(max_length=50)


class Location(models.Model):
    user = models.ForeignKey(User)
    geo_position = models.CharField(max_length=50)
