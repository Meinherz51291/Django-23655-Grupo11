from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('matafuegos/', views.matafuegos, name='matafuegos'), 
    path('estadisticas/', views.estadisticas, name='estadisticas'), 
    path('stock/', views.stock, name='stock'), 
    path('clientes/', views.clientes_listado , name='clientes'),
    path('clientes/detalle/<str:id_cliente>', views.clientes_detalle , name='clientes_detalle'),
    path('matafuegos/', views.matafuegos, name='matafuegos'), 
    ] 