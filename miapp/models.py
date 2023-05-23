from django.db import models

# Create your models here.

class Folios(models.Model):
    
    idEmpleado = models.CharField(max_length=255, verbose_name="Clave del seguridad")
    idAmallaves = models.CharField(max_length=255)
    idSeguridad = models.CharField(max_length=255)
    entrega = models.CharField(max_length=100)
    recibe = models.CharField(max_length=100)
    Area = models.CharField(max_length=255, verbose_name="donde se econtro")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    actualizo =models.DateField(auto_now=True, verbose_name="Actualizo el")
    objeto = models.CharField(max_length=125)
    valor = models.CharField(max_length=255)
    Content = models.TextField(verbose_name="Descripción")
    class Meta:
     verbose_name= "Folio"
     verbose_name_plural="Folios"

class empleado(models.Model):
    usuario = models.CharField(max_length=255, verbose_name="Usuario")
    password = models.CharField(max_length=255, verbose_name="contraseña")
    nombre = models.CharField(max_length=255, verbose_name="nombre")
    apellidop = models.CharField(max_length=255, verbose_name="apellido paterno")
    apellidom = models.CharField(max_length=255, verbose_name="apellido materno")
    tel = models.CharField(max_length=255, verbose_name="Telefono celular")
    area = models.CharField(max_length=255, verbose_name="Departamento de trabajo")
    puesto = models.CharField(max_length=255, verbose_name="puesto")
    claveHotel = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    actualizo =models.DateField(auto_now=True)
    class Meta:
     verbose_name= "Empleado"
     verbose_name_plural="empleados"
    
    def __str__(self):

       return f"{self.nombre} del area: {self.area}"


class seguridad(models.Model):
    nombre = models.CharField(max_length=255)
    apellidop = models.CharField(max_length=255)
    apellidom = models.CharField(max_length=255)
    cantidad = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    observaciones = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    actualizo =models.DateField(auto_now=True)
    class Meta:
      verbose_name= "Seguridad"
      verbose_name_plural="Seguridades"
    def __str__(self):

     return f"{self.nombre} del area: {self.actualizo}"



class amallaves(models.Model):
    nombre = models.CharField(max_length=255)
    apellidop = models.CharField(max_length=255)
    apellidom = models.CharField(max_length=255)
    cantidad = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    observaciones = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    actualizo =models.DateField(auto_now=True)
    class Meta:
     verbose_name= "Amallaves"
     verbose_name_plural="Amallave"
    def __str__(self):

     return f"{self.nombre} del area: {self.actualizo}"





