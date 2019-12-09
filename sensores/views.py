from rest_framework import viewsets
from .models import Datos
from .models import Movimientos
from .models import Reportes
from .serializers import DatosSerializer, MovimientosSerializer, ReportesSerializer
from datetime import date, time
from django.contrib import auth
from django.db.models import Sum
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
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

class DatosList(APIView):

    def get(self, request):

        dt = Datos.objects.latest('id')

        conten = [{
            "temperatura": dt.temperatura,
            "humedad": dt.humedad
        }]
        return Response(conten)

"""class ReportesList(generics.ListCreateAPIView):
    queryset = Reportes.objects.all()
    serializer_class = ReportesSerializer"""

class ReportesList(APIView):

    def get(self, request):

        dt = Reportes.objects.latest('id')

        conten = [{
            "usuario": dt.usuario.username,
            "temperatura_prom": dt.temperatura_prom,
            "humedad_prom": dt.humedad_prom,
            "periodo": dt.periodo,
            "descripcion": dt.descripcion,
            "ultima_Accion": dt.ultima_Accion,
            "fecha": dt.fecha,
            "hora": dt.hora
        }]
        return Response(conten)

class AccionesList(generics.ListCreateAPIView):
    queryset = Movimientos.objects.all()
    serializer_class = MovimientosSerializer

class ReportResponse(APIView):

    def get(self, request):

        getUsuario = request.GET.get('usuario',False)
        getPeriodo = request.GET.get('periodo',False)
        getDescripcion = request.GET.get('descripcion',False)
        getUltimaAccion = request.GET.get('ultimaAccion',False)
        intPeriodo = int(getPeriodo)

        try:
            usuarioF = User.objects.filter(username=getUsuario)[0]
            datosF = Datos.objects.all().order_by('-id')[:intPeriodo]

            tempF = datosF.aggregate(Sum('temperatura'))
            tempProm = round(tempF['temperatura__sum']/intPeriodo, 2)

            humF = datosF.aggregate(Sum('humedad'))
            humProm = round(humF['humedad__sum']/intPeriodo, 2)

            dt = Reportes(usuario=usuarioF,
                temperatura_prom=tempProm,
                humedad_prom=humProm,
                periodo=intPeriodo,
                descripcion=getDescripcion,
                ultima_Accion=getUltimaAccion,
                fecha=datetime.date.today(),
                hora=datetime.datetime.now().strftime('%H:%M:%S')
                )
            dt.save()
            conten = [{
                "Mensaje": "Add Success"
                }]
        except Exception as e:
            conten = [{
                "Mensaje": "An Error Has Ocurred"
                }]
        return Response(conten)

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


        dt = Movimientos.objects.get(id=1)
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

class DataResponse(APIView):

    def get(self, request):

        getTemperatura = request.GET.get('temperatura',False)
        getHumedad = request.GET.get('humedad',False)

        dt = Datos(temperatura=getTemperatura, humedad=getHumedad)
        dt.save()

        conten = [{
            "Mensaje": "Add Success"
        }]
        return Response(conten)