# Generated by Django 2.2.10 on 2020-03-09 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0012_auto_20200309_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modopago',
            name='creado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]