# Generated by Django 5.0.6 on 2024-06-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_stockrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=15)),
                ('especialidad', models.CharField(choices=[('materiales', 'Materiales'), ('herramientas_manuales', 'Herramientas Manuales'), ('herramientas_electricas', 'Herramientas Eléctricas'), ('herramientas_seguridad', 'Herramientas de Seguridad')], max_length=30)),
            ],
        ),
    ]
