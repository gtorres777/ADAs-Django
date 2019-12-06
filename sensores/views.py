from rest_framework import viewsets

from .serializers import ProductoSerializer, DatosSerializer, AccionesSerializer
from .models import Producto
from .models import Datos
from .models import Acciones

from rest_framework import generics

#testing

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes


class TokenResponse(APIView):
    #permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        
        temperatura = request.GET['temperatura']
        humedad = request.GET['humedad']

        datos = Datos.objects.get(id=1)
        datos.temperatura = temperatura
        datos.humedad = humedad
        datos.save()


        content = [{
            "Mensaje": "Update Success" 
        }]
        return Response(content)

class DatosList(generics.ListCreateAPIView):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('codigo')
    serializer_class = ProductoSerializer

class AccionesList(generics.ListCreateAPIView):
    queryset = Acciones.objects.all()
    serializer_class = AccionesSerializer

class ActionResponse(APIView):

    def get(self, request):
        
        accion = request.GET.get('accion',False)
        """pararse = request.GET.get('pararse',False)
        sentarse = request.GET.get('sentarse',False)"""
        
        pararse = 0
        sentarse = 0
        retroceder = 0
        avanzar = 0
        girarIzquierda = 0
        girarDerecha = 0
        saludar = 0
        bailar = 0

        if(accion == "reinicio"):
            pararse = 0
            sentarse = 0
            retroceder = 0
            avanzar = 0
            girarIzquierda = 0
            girarDerecha = 0
            saludar = 0
            bailar = 0
        if(accion == "pararse"):
            pararse = 1
        if(accion == "sentarse"):
            sentarse = 1
        if(accion == "avanzar"):
            avanzar = 1
        if(accion == "retroceder"):
            retroceder = 1
        if(accion == "girarIzquierda"):
            girarIzquierda = 1
        if(accion == "girarDerecha"):
            girarDerecha = 1
        if(accion == "saludar"):
            saludar = 1
        if(accion == "bailar"):
            bailar = 1
        

        dt = Acciones.objects.get(id=1)
        dt.pararse = pararse
        dt.sentarse = sentarse
        dt.retroceder = retroceder
        dt.avanzar = avanzar
        dt.girarIzquierda = girarIzquierda
        dt.girarDerecha = girarDerecha
        dt.saludar = saludar
        dt.bailar = bailar
        dt.save()

        conten = [{
            "Mensaje": "Update Success" 
        }]
        return Response(conten)