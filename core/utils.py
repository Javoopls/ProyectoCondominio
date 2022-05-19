import json
from . models import *

def carritoData(request):
    if request.user.is_authenticated:
        residente = request.user.residente
        reserva, created = Reserva.objects.get_or_create(
            residente=residente, pagada=False)
        espacios = reserva.cantreserva_set.all()
        espaciosCarrito = reserva.obtener_total_espacios
    else:
        espacios = []
        reserva = {'obtener_total_carrito': 0, 'obtener_total_espacios': 0, 'reservar': False}
        espaciosCarrito = reserva['obtener_total_espacios']
        
    return {'espaciosCarrito':espaciosCarrito, 'reserva':reserva, 'espacios':espacios}