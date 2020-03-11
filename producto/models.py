from django.db import models
from django.utils.html import format_html

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'catergoria_producto'
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='imagenes/productos/')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField(default=0.00)
    cantidad = models.PositiveIntegerField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def producto_img(self):
        return  format_html('<img src={} width="100px" height="auto"/>',self.img.url)


    class Meta:
        db_table = 'producto'
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return '{}'.format(self.nombre)