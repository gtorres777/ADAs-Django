from django.db import models

class Producto(models.Model):
     id_accion = models.AutoField(primary_key=True)
     accion = models.CharField(max_length=100)

class Datos(models.Model):
    temperatura = models.DecimalField(max_digits=10, decimal_places=2)
    humedad = models.DecimalField(max_digits=10, decimal_places=2)

class Acciones(models.Model):
     pararse = models.IntegerField()
     sentarse = models.IntegerField()

