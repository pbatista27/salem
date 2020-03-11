from django.contrib import admin
from .models import Contacto, Carrusel, Bancos, ModoPago
# Register your models here.


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'asunto', 'mensaje', 'respondido', 'creado')
    search_fields = ('correo',)

class CarruselAdmin(admin.ModelAdmin):
    list_display = ('img_carrusel','creado')

class BancosAdmin(admin.ModelAdmin):
    list_display = ('banco', 'img_banco','cuenta','tipo', 'nombre', 'cedula', 'estado')
    search_fields = ('banco','nombre','tipo')


class ModoPagoAmin(admin.ModelAdmin):
    list_display = ('nombre','creado_por')



admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Carrusel, CarruselAdmin)
admin.site.register(Bancos, BancosAdmin)
admin.site.register(ModoPago, ModoPagoAmin)
