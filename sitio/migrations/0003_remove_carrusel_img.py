# Generated by Django 2.2.10 on 2020-02-27 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0002_carrusel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrusel',
            name='img',
        ),
    ]
