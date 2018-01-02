"""straymap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from perfiles import views as perfiles_views
from mascotas import views as mascotas_views


admin.site.site_header = 'Proyecto EMA'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mascotas_views.home, name='home'),

    # Login y Registro
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^registro/$', perfiles_views.registro, name='registro'),
    url(r'^auth-login/$', perfiles_views.auth_login, name='auth_login'),
    url(r'^perfil/$', perfiles_views.perfil, name='perfil'),

    # AJAX
    url(r'^v1/mascotas/feed/$', mascotas_views.feed, name='feed'),
    url(r'^v1/mascotas/form/reporta/$',
        mascotas_views.reporta_mascota, name='reporta_mascota'),
    url(r'^v1/usuario/(?P<user_id>[\w\-]+)/$',
        perfiles_views.usuario, name='usuario'),

]
