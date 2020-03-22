from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import Inicio,  Contacto, Horoscopo, Bancos, Login
urlpatterns = [
    path('', Inicio.as_view(), name='sitio'),
    path('contactos/', Contacto.as_view(), name='contactos'),
    path('horoscopo/', Horoscopo.as_view(), name="horoscopo"),
    path('bancos/', Bancos.as_view(), name='bancos'),
    path('entrar/', Login.as_view(), name='entrar'),
    path('salir/', logout_then_login, name='salir'),
]