from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")

def matafuegos(request):
    return render(request, 'matafuegos.html')


def clientes_listado(request):
    return render(request, 'clientes.html')

def clientes_detalle(request, id_cliente):
    return HttpResponse(
        f"""
        <h1> Cliente ID:  {id_cliente} </h1>
        """
)

