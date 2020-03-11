from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



class Post(models.Model):
    STATUS_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado')
    )
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publicado')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    img = models.ImageField(upload_to='post/imagenes/')
    cuerpo = RichTextUploadingField()
    publicado = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=9, choices=STATUS_CHOICES, default='borrador')

    class Meta:
        ordering=('-publicado',)
        db_table='blog'

    def __str__(self):
        return self.titulo


