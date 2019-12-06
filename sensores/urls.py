from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sensores import views

from rest_framework.authtoken.views import obtain_auth_token
from sensores import views
from .views import DatosList



urlpatterns = [
    path('datos/', views.DatosList.as_view()),
    path('accion/',views.ActionResponse.as_view()),
    path('acciones/', views.AccionesList.as_view()),

    #Token
    path('token/', views.TokenResponse.as_view(), name='token'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
