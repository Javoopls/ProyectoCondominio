from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.decorators import residente_only
from .models import *

# Create your views here.


def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def espacio(request):
    espacios = Espacio.objects.all()
    context = {'espacios': espacios}
    return render(request, 'core/espacio.html', context)
    
def carrito(request):
    
    if request.user.is_authenticated:
        residente = request.user.residente
        reserva, created = Reserva.objects.get_or_create(residente=residente, pagada=False)
        espacios = reserva.cantreserva_set.all()
    else:
        espacios = []
    context = {'espacios':espacios}
    return render(request, 'core/carrito.html', context)

def pago(request):
    context = {}
    return render(request, 'core/pago.html', context)

def login_success(request):
    if request.user.groups.filter(name="admin").exists():
        return redirect('/admin/')
    else:
        return redirect('user')

@login_required(login_url='login')
@residente_only
def user(request):
    return render(request, 'core/user.html')
