from django.urls import path
from .views import Inicio,  Contacto, Login, Horoscopo, Bancos
urlpatterns = [
    path('', Inicio.as_view(), name='sitio'),
    path('contactos/', Contacto.as_view(), name='contactos'),
    path('entrar/', Login.as_view(), name="login"),
    path('horoscopo/', Horoscopo.as_view(), name="horoscopo" ),
    path('bancos/', Bancos.as_view(), name='bancos'),
]