from django.contrib import admin
from .models import Post

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publicado','estado')
    list_filter = ('estado', 'creado', 'publicado', 'autor')
    search_fields = ('titulo',)
    prepopulated_fields = {'slug':('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    ordering = ('estado','publicado')


admin.site.register(Post,PostAdmin)
