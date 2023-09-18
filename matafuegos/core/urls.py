from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('matafuegos/', views.matafuegos, name='matafuegos'), 
    path('clientes/', views.clientes_listado , name='clientes_listado'),
    path('clientes/detalle/<str:id_cliente>', views.clientes_detalle , name='clientes_detalle')
]   