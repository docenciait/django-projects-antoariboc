"""Creacion urls para Pizzas"""

from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    #homepage
    
    path('', views.index, name='index'),
    path('example/', views.example, name='example'),
]
