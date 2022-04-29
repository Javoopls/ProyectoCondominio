from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from core.decorators import residente_only
from core.models import Espacio

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def login_success(request):
    if request.user.groups.filter(name="admin").exists():
        return redirect('/admin/')
    else:
        return redirect('user')

@login_required(login_url='login')
@residente_only
def user(request):
    return render(request, 'core/user.html')


# Reservas
def espacios(request):
    if request.method == 'GET':
        espacios = Espacio.objects.all()
    datos = {
        'espacios' : espacios
    }
    return render(request, 'reserva/espacio.html', datos)

def disponibilidad(request,id):
    espacio = get_object_or_404(Espacio, id = id)
    datos = {
    # 'artista' : artista,
        'espacio' : espacio
    }
    # en argumento, pedir id del espacio
    # mostrar en url el nombre del espacio
    return render(request, 'reserva/disponibilidad.html', datos)

