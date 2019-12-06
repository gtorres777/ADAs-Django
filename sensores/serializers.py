from rest_framework import serializers
from .models import Producto,Datos,Acciones


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('codigo', 'accion')


class DatosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datos
        fields = ['id', 'temperatura', 'humedad']

class AccionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Acciones
        fields = ['id','pararse', 'sentarse']