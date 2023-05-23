# Generated by Django 3.0.5 on 2023-05-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amallaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellidop', models.CharField(max_length=255)),
                ('apellidom', models.CharField(max_length=255)),
                ('cantidad', models.CharField(max_length=255)),
                ('valor', models.CharField(max_length=255)),
                ('observaciones', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('actualizo', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('apellidop', models.CharField(max_length=255)),
                ('apellidom', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('puesto', models.CharField(max_length=255)),
                ('claveHotel', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('actualizo', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Folios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEmpleado', models.CharField(max_length=255)),
                ('idAmallaves', models.CharField(max_length=255)),
                ('idSeguridad', models.CharField(max_length=255)),
                ('entrega', models.CharField(max_length=100)),
                ('recibe', models.CharField(max_length=100)),
                ('Area', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('actualizo', models.DateField(auto_now=True)),
                ('objeto', models.CharField(max_length=125)),
                ('valor', models.CharField(max_length=255)),
                ('Content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='seguridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellidop', models.CharField(max_length=255)),
                ('apellidom', models.CharField(max_length=255)),
                ('cantidad', models.CharField(max_length=255)),
                ('valor', models.CharField(max_length=255)),
                ('observaciones', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('actualizo', models.DateField(auto_now=True)),
            ],
        ),
    ]