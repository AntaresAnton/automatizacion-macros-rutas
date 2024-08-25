# informes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anadir-informe/', views.anadir_informe, name='anadir_informe'),
    path('anadir-proceso/', views.anadir_proceso, name='anadir_proceso'),
    path('gestionar-informe/', views.gestionar_informes, name='gestionar_informes'),
    path('gestionar-procesos/', views.gestionar_procesos, name='gestionar_procesos'),
    path('logs/', views.logs, name='logs'),
    path('delete-report/<int:report_id>/', views.delete_report, name='delete_report'),
    path('edit-process/<int:process_id>/', views.edit_process, name='edit_process'),
    path('delete-process/<int:process_id>/', views.delete_process, name='delete_process'),
    path('edit-informe/<int:informe_id>/', views.edit_informe, name='edit_informe'),
    path('delete-informe/<int:informe_id>/', views.delete_informe, name='delete_informe'),
]

