from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.decorators import residente_only

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
    return render(request, 'reserva/espacio.html')
def disponibilidad(request):
    # en argumento, pedir id del espacio
    # mostrar en url el nombre del espacio
    return render(request, 'reserva/disponibilidad.html')