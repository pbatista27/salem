# Generated by Django 2.2.10 on 2020-03-07 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0006_bancos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bancos',
            options={'ordering': ['banco'], 'verbose_name': ('Banco',), 'verbose_name_plural': 'Bancos'},
        ),
        migrations.AlterModelTable(
            name='bancos',
            table='Bancos',
        ),
    ]