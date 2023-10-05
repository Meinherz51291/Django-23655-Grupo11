from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime
from .forms import AltaForms

def index(request):
    return render(request, "core/index.html")

def orden_pedido(request):
    return render(request, 'core/orden_pedido.html')

def orden_procesada (request):
    return render(request, 'core/orden_procesada.html')

def remito(request):
    return render(request, 'core/remito.html')

def estadisticas(request):
    return render(request, 'core/estadisticas.html')

def ordenes (request):
    return render(request, 'core/ordenes.html')


clientes_data = [
    {
        "id_pedido": "OP12345",
        "id_cliente": 1,
        "nombre": "Juan Pérez",
        "email": "juan.perez@example.com",
        "celular": "123-456-7890",
        "fecha_recarga": "2023-09-15",
        "fecha_vencimiento": "2024-09-15",
        "cantidad_matafuegos": 5,
        "tipo_matafuego": "2.5kg",
        "orden_procesada": True
    },
    {
        "id_pedido": "OP54321",
        "id_cliente": 2,
        "nombre": "María González",
        "email": "maria.gonzalez@example.com",
        "celular": "987-654-3210",
        "fecha_recarga": "2023-08-20",
        "fecha_vencimiento": "2024-08-20",
        "cantidad_matafuegos": 3,
        "tipo_matafuego": "1kg",
        "orden_procesada": False
    },
    {
        "id_pedido": "OP98765",
        "id_cliente": 3,
        "nombre": "Carlos Rodríguez",
        "email": "carlos.rodriguez@example.com",
        "celular": "555-555-5555",
        "fecha_recarga": "2023-10-10",
        "fecha_vencimiento": "2024-10-10",
        "cantidad_matafuegos": 10,
        "tipo_matafuego": "5kg",
        "orden_procesada": True
    },
    {
        "id_pedido": "OP67890",
        "id_cliente": 4,
        "nombre": "Ana Martínez",
        "email": "ana.martinez@example.com",
        "celular": "777-777-7777",
        "fecha_recarga": "2023-07-05",
        "fecha_vencimiento": "2024-07-05",
        "cantidad_matafuegos": 7,
        "tipo_matafuego": "10kg",
        "orden_procesada": True
    },
    {
        "id_pedido": "OP23456",
        "id_cliente": 5,
        "nombre": "Pedro López",
        "email": "pedro.lopez@example.com",
        "celular": "555-123-7890",
        "fecha_recarga": "2023-09-25",
        "fecha_vencimiento": "2024-11-25",
        "cantidad_matafuegos": 2,
        "tipo_matafuego": "2.5kg",
        "orden_procesada": False
    },
    {
        "id_pedido": "OP78901",
        "id_cliente": 6,
        "nombre": "Luisa Fernández",
        "email": "luisa.fernandez@example.com",
        "celular": "123-555-7890",
        "fecha_recarga": "2023-02-15",
        "fecha_vencimiento": "2024-12-15",
        "cantidad_matafuegos": 8,
        "tipo_matafuego": "5kg",
        "orden_procesada": False
    },
    {
        "id_pedido": "OP54321",
        "id_cliente": 7,
        "nombre": "Sofía Pérez",
        "email": "sofia.perez@example.com",
        "celular": "555-555-1234",
        "fecha_recarga": "2023-06-30",
        "fecha_vencimiento": "2024-06-30",
        "cantidad_matafuegos": 4,
        "tipo_matafuego": "1kg",
        "orden_procesada": True
    },
    {
        "id_pedido": "OP12309",
        "id_cliente": 8,
        "nombre": "Roberto Sánchez",
        "email": "roberto.sanchez@example.com",
        "celular": "444-444-4444",
        "fecha_recarga": "2023-05-10",
        "fecha_vencimiento": "2024-05-10",
        "cantidad_matafuegos": 6,
        "tipo_matafuego": "10kg",
        "orden_procesada": False
    },
    {
        "id_pedido": "OP56789",
        "id_cliente": 9,
        "nombre": "Elena García",
        "email": "elena.garcia@example.com",
        "celular": "999-888-7777",
        "fecha_recarga": "2023-04-15",
        "fecha_vencimiento": "2024-04-15",
        "cantidad_matafuegos": 1,
        "tipo_matafuego": "5kg",
        "orden_procesada": True
    },
    {
        "id_pedido": "OP09876",
        "id_cliente": 10,
        "nombre": "Hugo Rodríguez",
        "email": "hugo.rodriguez@example.com",
        "celular": "666-555-4444",
        "fecha_recarga": "2023-03-20",
        "fecha_vencimiento": "2024-03-20",
        "cantidad_matafuegos": 9,
        "tipo_matafuego": "2.5kg",
        "orden_procesada": True
    },
    {
        "id_pedido": "OP1122",
        "id_cliente": 11,
        "nombre": "Laura Martínez",
        "email": "laura.martinez@example.com",
        "celular": "777-888-9999",
        "fecha_recarga": "2023-02-10",
        "fecha_vencimiento": "2024-02-10",
        "matafuegos": [
            {"tipo": "1kg", "cantidad": 3},
            {"tipo": "5kg", "cantidad": 2}
        ],
        "orden_procesada": True
    },
    {
        "id_pedido": "OP1133",
        "id_cliente": 12,
        "nombre": "Andrés Pérez",
        "email": "andres.perez@example.com",
        "celular": "555-333-7777",
        "fecha_recarga": "2023-01-15",
        "fecha_vencimiento": "2024-01-15",
        "matafuegos": [
            {"tipo": "2.5kg", "cantidad": 4}
        ],
        "orden_procesada": False
    },
    {
        "id_pedido": "OP1144",
        "id_cliente": 13,
        "nombre": "Lucía Rodríguez",
        "email": "lucia.rodriguez@example.com",
        "celular": "888-999-4444",
        "fecha_recarga": "2023-12-20",
        "fecha_vencimiento": "2024-12-20",
        "matafuegos": [
            {"tipo": "10kg", "cantidad": 1}
        ],
        "orden_procesada": True
    },
    {
        "id_pedido": "OP1155",
        "id_cliente": 14,
        "nombre": "Diego Sánchez",
        "email": "diego.sanchez@example.com",
        "celular": "555-444-1111",
        "fecha_recarga": "2023-11-25",
        "fecha_vencimiento": "2024-11-25",
        "matafuegos": [
            {"tipo": "2.5kg", "cantidad": 3},
            {"tipo": "5kg", "cantidad": 2}
        ],
        "orden_procesada": True
    },
    {
        "id_pedido": "OP1166",
        "id_cliente": 15,
        "nombre": "Marta González",
        "email": "marta.gonzalez@example.com",
        "celular": "111-222-3333",
        "fecha_recarga": "2023-08-30",
        "fecha_vencimiento": "2024-10-30",
        "matafuegos": [
            {"tipo": "1kg", "cantidad": 2},
            {"tipo": "5kg", "cantidad": 1}
        ],
        "orden_procesada": False
    }
]


def clientes_listado(request):
    context = {
        "clientes": clientes_data  # Utiliza la lista de clientes definida en el archivo datos_clientes.py
    }
    return render(request, 'core/clientes.html', context)

def clientes_detalle(request, id_cliente):
    cliente = None
    for c in clientes_data:
        if c["id_cliente"] == int(id_cliente):  
            cliente = c
            break

    if cliente:
        context = {"cliente": cliente}
        return render(request, 'core/clientes_detalle.html', context)
    else:
        return HttpResponse("Cliente no encontrado", status=404)


def estadisticas_clientes(request):
    # Datos de ejemplo para las estadísticas
    grandes_clientes = ["Cliente 1", "Cliente 2", "Cliente 3"]
    clientes_particulares = ["Cliente A", "Cliente B", "Cliente C"]
    mejores_clientes = ["Mejor Cliente 1", "Mejor Cliente 2", "Mejor Cliente 3"]
    mejor_mes_venta = "Enero"
    ordenes_procesadas = 50
    ordenes_ejecutadas_mes_actual = 20
    ordenes_pendientes = 10

    context = {
        'grandes_clientes': grandes_clientes,
        'clientes_particulares': clientes_particulares,
        'mejores_clientes': mejores_clientes,
        'mejor_mes_venta': mejor_mes_venta,
        'ordenes_procesadas': ordenes_procesadas,
        'ordenes_ejecutadas_mes_actual': ordenes_ejecutadas_mes_actual,
        'ordenes_pendientes': ordenes_pendientes,
    }

    return render(request, 'core/estadisticas.html', context)

def ordenes_activas(clientes):
    clientes_activos = [cliente for cliente in clientes if not cliente["orden_procesada"]]
    return clientes_activos

def ordenes(request):
    # Supongamos que tienes una lista llamada 'clientes_data' con tus datos simulados
    clientes_activos = ordenes_activas(clientes_data)
    
    for cliente in clientes_activos:
        fecha_recarga = datetime.strptime(cliente["fecha_recarga"], "%Y-%m-%d")
        fecha_actual = datetime.now()
        diferencia = fecha_actual - fecha_recarga
        cliente["dias_corridos"] = diferencia.days
    
    context = {
        'clientes_activos': clientes_activos,
    }
    return render(request, 'core/ordenes.html', context)


    
def orden_detalle(request, id_pedido):
    orden_pedido = None
    for orden in clientes_data:
        if orden["id_pedido"] == id_pedido:
            orden_pedido = orden
            break

    if orden_pedido:
      
        context = {"orden_pedido": orden_pedido}
        return render(request, 'core/orden_detalle.html', context)
    else:
         return HttpResponse("Orden de Pedido no encontrado", status=404)
    



def alta_cliente(request):
    if request.method == 'POST':
        # Instanciamos un dato con valores
        formulario = AltaForms(request.POST)
        # Validamos
        if formulario.is_valid():
            # Aquí deberías guardar el cliente en la base de datos
            # Por ejemplo, si tienes un modelo Cliente:
            # cliente = formulario.save()
            # Luego puedes redirigir a la página de detalles del cliente o a donde desees
            return redirect(reverse('orden_pedido'))
    else:
        formulario = AltaForms()

    context = {
        'alta_cliente': formulario
    }
    return render(request, 'core/alta_cliente.html', context)