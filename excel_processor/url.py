from django.contrib import admin
from django.urls import path
from .views import excel, create_data, listagem

urlpatterns = [
    path('envia/', create_data , name='enviar'),
    path('listagem/', listagem , name='listagem'),
]
