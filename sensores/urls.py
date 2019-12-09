from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sensores import views

from rest_framework.authtoken.views import obtain_auth_token
from sensores import views
from .views import DatosList, ReportesList



urlpatterns = [
    path('datos/', views.DatosList.as_view()),
    path('dato/', views.DataResponse.as_view()),
    path('reportes/', views.ReportesList.as_view()),
    path('reporte/', views.ReportResponse.as_view()),
    path('accion/',views.ActionResponse.as_view()),
    path('acciones/', views.AccionesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
