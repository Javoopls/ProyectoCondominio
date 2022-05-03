from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from core.decorators import residente_only
from core.models import Espacio, ReservasHorario

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

# -------------------------------------------------------------------
# MODULO: Login
# -------------------------------------------------------------------
def login_success(request):
    if request.user.groups.filter(name="admin").exists():
        return redirect('/admin/')
    else:
        return redirect('user')

@login_required(login_url='login')
@residente_only
def user(request):
    return render(request, 'core/user.html')

# -------------------------------------------------------------------
# MODULO: Reservas
# -------------------------------------------------------------------
@login_required(login_url='login')
@residente_only
def espacios(request):
    if request.method == 'GET':
        espacios = Espacio.objects.all()
    datos = {
        'espacios' : espacios
    }
    return render(request, 'reserva/espacio.html', datos)

@login_required(login_url='login')
@residente_only
def disponibilidad(request,id):
    from datetime import datetime
    espacio = get_object_or_404(Espacio, id = id)
    horarios = ReservasHorario.objects.all()

    rangoM = []
    rangoT = []
    rangoW = []
    rangoTh = []
    rangoF = []
    rangoSa = []
    rangoSu = []
    for i in range(0, horarios.count()):
        d = horarios[i]
        if (d.day == 'Monday'):
            s = d.inicio.hour
            t = d.termino.hour 
            for k in range(0, t-s):
                hr = s+k+1
                if (hr >= 12):
                    sigla = 'p.m.'
                else:
                    sigla = 'a.m.'
                rangoM.append(str(hr) + ' ' + sigla)
        if (d.day == 'Tuesday'):
            s = d.inicio.hour
            t = d.termino.hour 
            for k in range(0, t-s):
                hr = s+k+1
                if (hr >= 12):
                    sigla = 'p.m.'
                else:
                    sigla = 'a.m.'
                rangoT.append(str(hr) + ' ' + sigla)
        if (d.day == 'Wednesday'):
            s = d.inicio.hour
            t = d.termino.hour 
            for k in range(0, t-s):
                hr = s+k+1
                if (hr >= 12):
                    sigla = 'p.m.'
                else:
                    sigla = 'a.m.'
                rangoW.append(str(hr) + ' ' + sigla)
        if (d.day == 'Thursday'):
            s = d.inicio.hour
            t = d.termino.hour 
            for k in range(0, t-s):
                hr = s+k+1
                if (hr >= 12):
                    sigla = 'p.m.'
                else:
                    sigla = 'a.m.'
                rangoTh.append(str(hr) + ' ' + sigla)
        if (d.day == 'Friday'):
            s = d.inicio.hour
            t = d.termino.hour 
            for k in range(0, t-s):
                hr = s+k+1
                if (hr >= 12):
                    sigla = 'p.m.'
                else:
                    sigla = 'a.m.'
                rangoF.append(str(hr) + ' ' + sigla)
        if (d.day == 'Saturday'):
            s = d.inicio.hour
            t = d.termino.hour 
            for k in range(0, t-s):
                hr = s+k+1
                if (hr >= 12):
                    sigla = 'p.m.'
                else:
                    sigla = 'a.m.'
                rangoSa.append(str(hr) + ' ' + sigla)
        else:
            if (d.day == 'Sunday'):
                s = d.inicio.hour
                t = d.termino.hour 
                for k in range(0, t-s):
                    hr = s+k+1
                    if (hr >= 12):
                        sigla = 'p.m.'
                    else:
                        sigla = 'a.m.'
                    rangoSu.append(str(hr) + ' ' + sigla)

    hoy = datetime.today()
    dia = hoy.strftime('%A')

    datos = {
    # 'artista' : artista,
        'espacio' : espacio,
        'horarios': horarios,
        'rangoM': rangoM,
        'rangoT': rangoT,
        'rangoW': rangoW,
        'rangoTh': rangoTh,
        'rangoF': rangoF,
        'rangoSa': rangoSa,
        'rangoSu': rangoSu,
        'dia': dia
    }

    # FALTA: cálculo de Aforos
    
    return render(request, 'reserva/disponibilidad.html', datos)

# -------------------------------------------------------------------
# MODULO: Conserjería
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# MODULO: Gastos Comunes
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# MODULO: Avisos y alertas
# -------------------------------------------------------------------