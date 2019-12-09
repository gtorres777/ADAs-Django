from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Datos, Movimientos, Reportes

class DatosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datos
        fields = ['id', 'temperatura', 'humedad']

class MovimientosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movimientos
        fields = ['id','pararse', 'sentarse','retroceder','avanzar','girarIzquierda','girarDerecha','saludar','bailar']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    reportes = serializers.PrimaryKeyRelatedField(many=True, queryset=Reportes.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username','reportes']

class ReportesSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    class Meta:
        model = Reportes
        fields = ['id', 'usuario', 'temperatura_prom','humedad_prom','periodo','descripcion','ultima_Accion']