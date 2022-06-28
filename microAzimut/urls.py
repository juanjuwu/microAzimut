from django.urls import path
from microAzimut import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculo/', views.calculo, name='calculo'),
]