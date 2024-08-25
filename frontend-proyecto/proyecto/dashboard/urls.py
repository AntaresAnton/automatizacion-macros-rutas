from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anadir-informe/', views.anadir_informe, name='anadir_informe'),
    path('anadir-proceso/', views.anadir_proceso, name='anadir_proceso'),
    path('gestionar-informe/', views.gestionar_informe, name='gestionar_informe'),
    path('gestionar-proceso/', views.gestionar_proceso, name='gestionar_proceso'),
    path('log/', views.log, name='log'),
]
