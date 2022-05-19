from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from core.decorators import residente_only
from .models import *
import json
import datetime
from . utils import carritoData

# Create your views here.


def home(request):

    data = carritoData(request)
    espaciosCarrito = data['espaciosCarrito']

    espacios = Espacio.objects.all()
    context = {'espacios': espacios, 'espaciosCarrito': espaciosCarrito}
    return render(request, 'core/home.html', context)


def espacio(request):

    data = carritoData(request)
    espaciosCarrito = data['espaciosCarrito']

    espacios = Espacio.objects.all()
    context = {'espacios': espacios, 'espaciosCarrito': espaciosCarrito}
    return render(request, 'core/espacio.html', context)


def carrito(request):

    data = carritoData(request)
    espacios = data['espacios']
    reserva = data['reserva']
    espaciosCarrito = data['espaciosCarrito']

    context = {'espacios': espacios, 'reserva': reserva,
               'espaciosCarrito': espaciosCarrito}
    return render(request, 'core/carrito.html', context)

def pago(request):

    data = carritoData(request)
    espacios = data['espacios']
    reserva = data['reserva']
    espaciosCarrito = data['espaciosCarrito']

    context = {'espacios': espacios, 'reserva': reserva,
               'espaciosCarrito': espaciosCarrito}
    return render(request, 'core/pago.html', context)


def login_success(request):
    if request.user.groups.filter(name="admin").exists():
        return redirect('/admin/')
    else:
        return redirect('user')


@login_required(login_url='login')
@residente_only
def user(request):
    data = carritoData(request)
    espaciosCarrito = data['espaciosCarrito']

    espacios = Espacio.objects.all()
    context = {'espacios': espacios, 'espaciosCarrito': espaciosCarrito}
    return render(request, 'core/user.html', context)


def updateReserva(request):
    data = json.loads(request.body)
    espacioId = data['espacioId']
    action = data['action']
    print('Action:', action)
    print('espacioId:', espacioId)

    residente = request.user.residente
    espacio = Espacio.objects.get(id=espacioId)
    reserva, created = Reserva.objects.get_or_create(
        residente=residente, pagada=False)

    cantReserva, created = CantReserva.objects.get_or_create(
        reserva=reserva, espacio=espacio)

    if action == 'add':
        cantReserva.cantidad = (cantReserva.cantidad + 1)
    elif action == 'remove':
        cantReserva.cantidad = (cantReserva.cantidad - 1)

    cantReserva.save()

    if cantReserva.cantidad <= 0:
        cantReserva.delete()

    return JsonResponse('Espacio Aniadido', safe=False)

def procesarReserva(request):
    id_reserva = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        residente = request.user.residente
        reserva, created = Reserva.objects.get_or_create(residente=residente, pagada=False)

    else:
        print('Usuario no logeado')

    total = float(data['form']['total'])
    reserva.id_reserva = id_reserva

    if total == reserva.obtener_total_carrito:
        reserva.pagada = True
    reserva.save()

    if reserva.reservar == True:
        PagoReserva.objects.create(
            residente = residente,
            reserva = reserva,
            fecha_reserva=data['reservar']['fecha'],
            hora_reserva=data['reservar']['hora'],
        )

    print('Data:',request.body)
    return JsonResponse('Pago Completado', safe=False)
