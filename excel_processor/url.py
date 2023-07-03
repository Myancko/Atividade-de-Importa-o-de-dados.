from django.contrib import admin
from django.urls import path
from .views import excel

urlpatterns = [
    path('envia/', excel , name='enviar'),
]
