from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','categoria','nombre','producto_img','descripcion','precio','cantidad','estado')
    search_fields = ('nombre',)
    list_display_links = ('nombre',)
    list_editable = ('estado','precio','cantidad')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','creado')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)