from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from core.decorators import residente_only, conserje_only
from core.forms import EventoForm
from .models import *
import json
import datetime
from . utils import carritoData

# Create your views here.


def home(request):
    return render(request, 'core/home.html')

    # data = carritoData(request)
    # espaciosCarrito = data['espaciosCarrito']

    # espacios = Espacio.objects.all()
    # context = {'espacios': espacios, 'espaciosCarrito': espaciosCarrito}
    # return render(request, 'core/home.html', context)

@login_required(login_url='login')
@residente_only
def espacio(request):

    data = carritoData(request)
    espaciosCarrito = data['espaciosCarrito']

    espacios = Espacio.objects.all()
    context = {'espacios': espacios, 'espaciosCarrito': espaciosCarrito}
    return render(request, 'core/espacio.html', context)

@login_required(login_url='login')
@residente_only
def carrito(request):

    data = carritoData(request)
    espacios = data['espacios']
    reserva = data['reserva']
    espaciosCarrito = data['espaciosCarrito']

    context = {'espacios': espacios, 'reserva': reserva,
               'espaciosCarrito': espaciosCarrito}
    return render(request, 'core/carrito.html', context)

@login_required(login_url='login')
@residente_only
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
@conserje_only
def conserjeView(request):
    if request.user.is_authenticated:
        conserje = str(request.user.conserje.id)
        print(conserje)
        print(type(conserje))
    datos={
        'conserje': conserje
    }
    return render(request, 'core/userConserje.html')

@login_required(login_url='login')
@residente_only
def user(request):
    data = carritoData(request)
    espaciosCarrito = data['espaciosCarrito']

    espacios = Espacio.objects.all()
    context = {'espacios': espacios, 'espaciosCarrito': espaciosCarrito}
    return render(request, 'core/user.html', context)


@login_required(login_url='login')
@residente_only
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

@login_required(login_url='login')
@residente_only
def procesarReserva(request):
    id_reserva = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        residente = request.user.residente
        reserva, created = Reserva.objects.get_or_create(residente=residente, pagada=False)

    else:
        print('Usuario no logeado')

    total = data['form']['total']
    reserva.id_reserva = id_reserva

    if total == reserva.obtener_total_carrito:
        reserva.pagada = True
    reserva.save()

    if reserva.compReserva == True:
        PagoReserva.objects.create(
            residente = residente,
            reserva = reserva,
            fecha_reserva=data['reserva']['fecha'],
            hora_reserva=data['reserva']['hora'],
        )

    print('Data:',request.body)
    return JsonResponse('Pago Completado', safe=False)


@login_required(login_url='login')
@conserje_only
def eventoLibroAdd(request,id):
    if request.user.is_authenticated:
        conserje = Conserje.objects.get(id=id)
        print(conserje)

    datos = {
        'form': EventoForm()
    }

    if request.method == 'POST':
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            evento = formulario.save(commit=False)
            evento.conserje = conserje
            print(formulario)
            evento.save()
            return redirect("/conserje")
    else:
        formulario = EventoForm()
        
    return render(request, 'libro/libro.html',datos)


def listarEvento(request,id):
    eventos = EventoLibro.objects.filter(conserje=id).order_by('fecha')

    datos = {
        'eventos': eventos
    }

    return render(request, 'libro/listar.html', datos)


def editarEvento(request,id):
    evento = EventoLibro.objects.get(id=id)

    datos = {
        'form': EventoForm(instance=evento)
    }

    if request.method == 'POST':
        formulario = EventoForm(data=request.POST, instance=evento)
        if formulario.is_valid():
            formulario.save()
            return redirect("/conserje")

    return render(request, 'libro/editar.html', datos)