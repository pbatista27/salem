from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Producto
# Create your views here.


class Producto(ListView):
    template_name = 'producto.html'
    model = Producto
    queryset = Producto.objects.filter(estado=True).all()

class ProductoDetalle(DetailView):
    template_name = 'producto-detalle.html'

