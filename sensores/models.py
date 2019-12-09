from django.db import models
from django.contrib import auth
from datetime import date, time
from django.utils import timezone

class Reportes(models.Model):
     usuario = models.ForeignKey('auth.User', related_name='reportes', on_delete=models.CASCADE)
     temperatura_prom = models.DecimalField(max_digits=10, decimal_places=2)
     humedad_prom = models.DecimalField(max_digits=10, decimal_places=2)
     periodo = models.IntegerField()
     descripcion = models.CharField(max_length=200)
     ultima_Accion = models.CharField(max_length=45)
     fecha = models.DateField(default=date.today)
     hora = models.TimeField(default=timezone.now)

class Datos(models.Model):
    temperatura = models.DecimalField(max_digits=10, decimal_places=2)
    humedad = models.DecimalField(max_digits=10, decimal_places=2)

class Movimientos(models.Model):
     pararse = models.IntegerField()
     sentarse = models.IntegerField()
     avanzar = models.IntegerField()
     retroceder = models.IntegerField()
     girarIzquierda = models.IntegerField()
     girarDerecha = models.IntegerField()
     saludar = models.IntegerField()
     bailar = models.IntegerField()


