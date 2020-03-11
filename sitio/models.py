from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.http import request

# Create your models here.

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    asunto = models.CharField(max_length=70)
    mensaje = models.TextField()
    respondido = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']
        db_table = "contacto"

    def __str__(self):
        return "{} {} {}".format(self.correo, self.nombre, self.apellido)

class Carrusel(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='imagenes/carrusel/')
    creado = models.DateTimeField(auto_now_add=True)

    def img_carrusel(self):
        return format_html('<img src={} width="120px" height="auto"/>', self.img.url)

    class Meta:
        db_table = "carrusel"
        verbose_name = "Carrusel"
        verbose_name_plural = "Carruseles"
        ordering = ['creado']

    def __str__(self):
        return str(self.img)


class Bancos(models.Model):

    TIPO_CUENTA = [('',''),('corriente','Corriente'), ('ahorro','Ahorro')]

    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='imagenes/bancos/')
    banco = models.CharField(max_length=100)
    cuenta = models.CharField(max_length=20)
    tipo = models.CharField(choices=TIPO_CUENTA, blank=True, null=True, max_length=9)
    nombre = models.CharField(max_length=75)
    cedula = models.CharField(max_length=10)
    estado = models.BooleanField(default=0)


    def img_banco(self):
        return format_html('<img src={} width="120px" height="auto"/>', self.img.url)

    class Meta:
        db_table = 'Bancos'
        verbose_name='Banco',
        verbose_name_plural = 'Bancos'
        ordering= ['banco']

    def __str__(self):
        return "{}".format(self.banco)

class ModoPago(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    creado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table= 'modo_pago'
        verbose_name= 'ModoPago'
        verbose_name_plural= 'ModoPagos'
        ordering=['nombre']

    def __str__(self):
        return self.nombre


class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    numero_pago = models.IntegerField(unique=True)
    modo_pago = models.ForeignKey(ModoPago, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete= models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
