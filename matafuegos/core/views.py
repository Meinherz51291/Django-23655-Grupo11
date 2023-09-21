from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "core/index.html")

def matafuegos(request):
    return render(request, 'core/matafuegos.html')

def estadisticas(request):
    return render(request, 'core/estadisticas.html')

def stock (request):
    return render(request, 'core/stock.html')


def clientes_listado(request):
    context ={
    
    "clientes": [
        {
            "id_cliente": 1,
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juan.perez@example.com",
            "celular": "123-456-7890",
            "cliente_activo": True
        },
        {
            "id_cliente": 2,
            "nombre": "María",
            "apellido": "González",
            "email": "maria.gonzalez@example.com",
            "celular": "987-654-3210",
            "cliente_activo": False
        },
        {
            "id_cliente": 3,
            "nombre": "Carlos",
            "apellido": "Rodríguez",
            "email": "carlos.rodriguez@example.com",
            "celular": "555-555-5555",
            "cliente_activo": True
        },
        {
            "id_cliente": 4,
            "nombre": "Ana",
            "apellido": "Martínez",
            "email": "ana.martinez@example.com",
            "celular": "777-777-7777",
            "cliente_activo": True
        }
    ]
    }
    return render(request, 'core/clientes.html', context)

def clientes_detalle(request, id_cliente):
    
    clientes = [
       
    ]

    
    cliente = None
    for c in clientes:
        if c["id_cliente"] == id_cliente:
            cliente = c
            break

    if cliente:
        context = {"cliente": cliente}
        return render(request, 'core/clientes_detalle.html', context)
    else:
        
        return HttpResponse("Cliente no encontrado", status=404)

