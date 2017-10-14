# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0007_mascota_raza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tamaño',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamaño', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tamño',
                'verbose_name_plural': 'Tamaños de mascotas',
            },
        ),
        migrations.AddField(
            model_name='mascota',
            name='tamaño',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mascotas.Tamaño'),
            preserve_default=False,
        ),
    ]
