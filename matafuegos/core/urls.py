from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('orden_pedido/', views.orden_pedido, name='orden_pedido'), 
    path('orden_pedido/<str:id_pedido>', views.orden_detalle, name='orden_detalle'),
    path('orden_procesada/', views.orden_procesada, name='orden_procesada'), 
    path('estadisticas/', views.estadisticas, name='estadisticas'), 
    path('estadisticas/ordenes/', views.ordenes, name='ordenes'), 
    path('remito/', views.remito, name='remito'),  
    path('clientes/', views.clientes_listado , name='clientes'),
    path('clientes/detalle/<str:id_cliente>/', views.clientes_detalle, name='clientes_detalle'),
    
    ] 