from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from core.decorators import residente_only, conserje_only, directiva_only
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
        if (espacio.nombre == 'Quincho' or espacio.nombre == 'Sala Eventos'):
            if (d.day == 'Friday'):
                hr = 0
                s = d.inicio.hour
                t = d.termino.hour
                for k in range(0, 18, 4):
                    if (hr < 18-4):
                        hr = s+k
                        if (hr >= 12):
                            sigla = 'p.m.'
                        else:
                            sigla = 'a.m.'
                    else:
                        break 
                    rangoF.append(str(hr) + ' ' + sigla)
                    
            if (d.day == 'Saturday'):
                hr = 0
                s = d.inicio.hour
                t = d.termino.hour
                for k in range(0, 18, 4):
                    if (hr < 18-4):
                        hr = s+k
                        if (hr >= 12):
                            sigla = 'p.m.'
                        else:
                            sigla = 'a.m.'
                    else:
                        break
                    rangoSa.append(str(hr) + ' ' + sigla)
            else:
                if (d.day == 'Sunday'):
                    hr = 0
                    s = d.inicio.hour
                    t = d.termino.hour
                    for k in range(0, t-s, 4):
                        if (hr < 14-4):
                            hr = s+k
                            if (hr >= 12):
                                sigla = 'p.m.'
                            else:
                                sigla = 'a.m.'
                        else:
                            break
                        rangoSu.append(str(hr) + ' ' + sigla)
        else:
            if (d.day == 'Monday'):
                s = d.inicio.hour
                t = d.termino.hour
                for k in range(0, t-s, 1):
                    hr = s+k
                    if (hr >= 12):
                        sigla = 'p.m.'
                    else:
                        sigla = 'a.m.'
                    rangoM.append(str(hr) + ' ' + sigla)
            if (d.day == 'Tuesday'):
                s = d.inicio.hour
                t = d.termino.hour
                for k in range(0, t-s, 1):
                    hr = s+k
                    if (hr >= 12):
                        sigla = 'p.m.'
                    else:
                        sigla = 'a.m.'
                    rangoT.append(str(hr) + ' ' + sigla)
            if (d.day == 'Wednesday'):
                s = d.inicio.hour
                t = d.termino.hour
                for k in range(0, t-s, 1):
                    hr = s+k
                    if (hr >= 12):
                        sigla = 'p.m.'
                    else:
                        sigla = 'a.m.'
                    rangoW.append(str(hr) + ' ' + sigla)
            if (d.day == 'Thursday'):
                s = d.inicio.hour
                t = d.termino.hour
                for k in range(0, t-s, 1):
                    hr = s+k
                    if (hr >= 12):
                        sigla = 'p.m.'
                    else:
                        sigla = 'a.m.'
                    rangoTh.append(str(hr) + ' ' + sigla)
            if (d.day == 'Friday'):
                hr = 0
                s = d.inicio.hour
                t = d.termino.hour
                for k in range(0, 18, 1):
                    if (hr < 18-1):
                        hr = s+k
                        if (hr >= 12):
                            sigla = 'p.m.'
                        else:
                            sigla = 'a.m.'
                    else:
                        break 
                    rangoF.append(str(hr) + ' ' + sigla)
                    
            if (d.day == 'Saturday'):
                hr = 0
                s = d.inicio.hour
                t = d.termino.hour
                for k in range(0, 18, 1):
                    if (hr < 18-1):
                        hr = s+k
                        if (hr >= 12):
                            sigla = 'p.m.'
                        else:
                            sigla = 'a.m.'
                    else:
                        break
                    rangoSa.append(str(hr) + ' ' + sigla)
            else:
                if (d.day == 'Sunday'):
                    hr = 0
                    s = d.inicio.hour
                    t = d.termino.hour
                    for k in range(0, t-s, 1):
                        hr = s+k
                        if (hr >= 12):
                            sigla = 'p.m.'
                        else:
                            sigla = 'a.m.'
                        rangoSu.append(str(hr) + ' ' + sigla)


# ================
# RESPALDO CICLO
# ================
    # for i in range(0, horarios.count()):
    #     d = horarios[i]
    #     if (d.day == 'Monday'):
    #         s = d.inicio.hour
    #         t = d.termino.hour
    #         for k in range(0, t-s):
    #             hr = s+k+1
    #             if (hr >= 12):
    #                 sigla = 'p.m.'
    #             else:
    #                 sigla = 'a.m.'
    #             rangoM.append(str(hr) + ' ' + sigla)
    #     if (d.day == 'Tuesday'):
    #         s = d.inicio.hour
    #         t = d.termino.hour
    #         for k in range(0, t-s):
    #             hr = s+k+1
    #             if (hr >= 12):
    #                 sigla = 'p.m.'
    #             else:
    #                 sigla = 'a.m.'
    #             rangoT.append(str(hr) + ' ' + sigla)
    #     if (d.day == 'Wednesday'):
    #         s = d.inicio.hour
    #         t = d.termino.hour
    #         for k in range(0, t-s):
    #             hr = s+k+1
    #             if (hr >= 12):
    #                 sigla = 'p.m.'
    #             else:
    #                 sigla = 'a.m.'
    #             rangoW.append(str(hr) + ' ' + sigla)
    #     if (d.day == 'Thursday'):
    #         s = d.inicio.hour
    #         t = d.termino.hour
    #         for k in range(0, t-s):
    #             hr = s+k+1
    #             if (hr >= 12):
    #                 sigla = 'p.m.'
    #             else:
    #                 sigla = 'a.m.'
    #             rangoTh.append(str(hr) + ' ' + sigla)
    #     if (d.day == 'Friday'):
    #         s = d.inicio.hour
    #         t = d.termino.hour
    #         for k in range(0, t-s):
    #             hr = s+k+1
    #             if (hr >= 12):
    #                 sigla = 'p.m.'
    #             else:
    #                 sigla = 'a.m.'
    #             rangoF.append(str(hr) + ' ' + sigla)
    #     if (d.day == 'Saturday'):
    #         s = d.inicio.hour
    #         t = d.termino.hour
    #         for k in range(0, t-s):
    #             hr = s+k+1
    #             if (hr >= 12):
    #                 sigla = 'p.m.'
    #             else:
    #                 sigla = 'a.m.'
    #             rangoSa.append(str(hr) + ' ' + sigla)
    #     else:
    #         if (d.day == 'Sunday'):
    #             s = d.inicio.hour
    #             t = d.termino.hour
    #             for k in range(0, t-s):
    #                 hr = s+k+1
    #                 if (hr >= 12):
    #                     sigla = 'p.m.'
    #                 else:
    #                     sigla = 'a.m.'
    #                 rangoSu.append(str(hr) + ' ' + sigla)
# ================
# RESPALDO CICLO
# ================

    # importando librería para determinar las fechas y días
    import datetime
    from datetime import timedelta, date
    hoy = date.today()
    current_day = hoy.strftime('%A')

    if(hoy.weekday() == 0):
        # es lunes
        start = hoy.day
        end = (hoy + datetime.timedelta(days=+6)).day
    elif(hoy.weekday() == 1):
        # es martes
        start = (hoy + datetime.timedelta(days=-1)).day
        end = (hoy + datetime.timedelta(days=+5)).day
    elif(hoy.weekday() == 2):
        # es miercoles
        start = (hoy + datetime.timedelta(days=-2)).day
        end = (hoy + datetime.timedelta(days=+4)).day
    elif(hoy.weekday() == 3):
        # es jueves
        start = (hoy + datetime.timedelta(days=-3)).day
        end = (hoy + datetime.timedelta(days=+3)).day
    elif(hoy.weekday() == 4):
        # es viernes
        start = (hoy + datetime.timedelta(days=-4)).day
        end = (hoy + datetime.timedelta(days=+2)).day
    elif(hoy.weekday() == 5):
        # es sabado
        start = (hoy + datetime.timedelta(days=-5)).day
        end = (hoy + datetime.timedelta(days=+1)).day
    else:
        # es domingo
        start = (hoy + datetime.timedelta(days=-6)).day
        end =  hoy.day

    month = hoy.strftime('%B')
    date = str(month)+ ': Mon.' + str(start) +' - '+'Sun.' + str(end)
 

# =============
# DICCIONARIO
# =============
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
        'current_day': current_day,
        'date': date
    }

    # FALTA: cálculo de Aforos
    
    return render(request, 'reserva/disponibilidad.html', datos)


def cart(request):
    return render(request, 'reserva/cart.html')

# -------------------------------------------------------------------
# MODULO: Conserjería
# -------------------------------------------------------------------
@login_required(login_url='login')
@conserje_only
def conserjeView(request):
    return render(request, 'core/userConserje.html')


# -------------------------------------------------------------------
# MODULO: Gastos Comunes
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# MODULO: Avisos y alertas
# -------------------------------------------------------------------