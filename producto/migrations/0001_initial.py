# Generated by Django 2.2.10 on 2020-02-29 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'verbose_name': 'Categoria',
                'db_table': 'catergoria_producto',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='imagenes/productos/')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.FloatField(default=0.0)),
                ('cantidad', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Producutos',
                'verbose_name': 'Producto',
                'db_table': 'producto',
            },
        ),
    ]
