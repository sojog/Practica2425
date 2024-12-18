from django.urls import path
from .views import *

urlpatterns = [
     path('', joaca_jocul),
     path('verifica', verifica_tara_view, name='verifica_url')     
]