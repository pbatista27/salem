from django.conf import settings
from django.core.mail import EmailMessage
from django.http.response import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import ContactoForm
import requests
import json
from .models import Carrusel, Bancos
# Create your views here.

class Inicio(TemplateView):
    template_name = 'inicio.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = Carrusel.objects.all()
        return context

class Contacto(FormView):
    form_class = ContactoForm
    template_name = 'contactos.html'
    success_url = reverse_lazy('sitio:contactos')


    def form_valid(self, form):
        form.nombre = form.cleaned_data['nombre']
        form.apellido = form.cleaned_data['apellido']
        form.correo = form.cleaned_data['correo']
        form.asunto = form.cleaned_data['asunto']
        form.mensaje = form.cleaned_data['mensaje']
        form.save()
        try:
            self.enviar_email(form)
            self.enviar_correo_usuario(form)
        except:
            print('falla al enviar correo electronico')
        return super().form_valid(form)

    def enviar_email(self, form):
        body = render_to_string('correo_contacto.html',{
            'usuario': form.nombre +' '+ form.apellido,
            'correo': form.correo,
            'asunto': form.asunto,
            'mensaje': form.mensaje
        })

        email_mensaje = EmailMessage(
            subject= form.asunto,
            body= body,
            from_email= settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER]
        )

        email_mensaje.content_subtype = 'html'
        email_mensaje.send()

    def enviar_correo_usuario(self, form):
        body = render_to_string('correo_contacto_usuario.html',{
            'usuario': form.nombre+ ' '+ form.apellido,
            'asunto': form.asunto
        })
        email_mensaje_usuario = EmailMessage(
            subject='Saludos',
            body= body,
            from_email= settings.EMAIL_HOST_USER,
            to=[form.correo]
        )

        email_mensaje_usuario.content_subtype = 'html'
        email_mensaje_usuario.send()

class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('tablero:tablero')

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        # Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)






class Horoscopo(TemplateView):
    template_name = 'horoscopo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        horoscopo = self.get_horoscopo()
        if horoscopo:
            context['titulo'] = horoscopo['titulo']
            context['horoscopos'] = horoscopo['horoscopo']
        return context

    def get_horoscopo(self):
        try:
            res = requests.get('https://api.adderou.cl/tyaas/',{})
            horoscopo = json.loads(res.text)
            return horoscopo

        except Exception as e:
            print(e)

class Bancos(ListView):

    model = Bancos
    context_object_name = 'bancos'
    template_name = 'bancos/banco_list.html'
    queryset = Bancos.objects.filter(estado=True)