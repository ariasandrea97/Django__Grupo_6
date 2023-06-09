# Generated by Django 4.2.1 on 2023-05-23 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_hotel', models.CharField(max_length=128, verbose_name='Hotel')),
                ('direccion', models.CharField(max_length=128, verbose_name='Direccion')),
                ('categoria', models.IntegerField(verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=128)),
                ('hotel', models.ManyToManyField(to='Viajeros.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registracion', models.DateField(null=True)),
                ('fecha_desde', models.DateField(null=True)),
                ('fecha_hasta', models.DateField(null=True)),
                ('usuario', models.CharField(max_length=128, verbose_name='usuario ')),
                ('Tipo_reserva', models.CharField(choices=[('Alojamiento', 'Alojamiento'), ('Excursion', 'Excursion'), ('Gastronomia', 'Gastronomia')], default='Alojamiento', max_length=15, verbose_name='Tipo de reserva')),
                ('adulto', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=2, verbose_name='Cantidad de Adultos')),
                ('menor', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Cantidad de Menores')),
                ('estado', models.BooleanField(default=True)),
                ('hotel', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='Viajeros.hotel')),
            ],
        ),
    ]
