from django.http import HttpResponse
from django.shortcuts import redirect

# Decorators: manipular los accesos permitidos
# Forma 1 de accesar según roles
# def allowded_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):

#             # para verificar x consola quien se conecta
#             print('Conectado: ', allowed_roles)

#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('No estás autorizado para ver esta página')

#             return view_func(request, *args, **kwargs)
#         return wrapper_func
#     return decorator


# Forma 2 de accesar según roles, más específica con redirects
def residente_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin':
            return redirect('/admin/')

        if group == 'conserje':
            return redirect('conserje')

        if group == 'directiva':
            return redirect('userDire')

        if group == 'residente':
            return view_func(request, *args, **kwargs)

    return wrapper_func

def conserje_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin':
            return redirect('/admin/')

        if group == 'residente':
            return redirect('user')

        if group == 'directiva':
            return redirect('userDire')
        
        if group == 'conserje':
            return view_func(request, *args, **kwargs)
    return wrapper_func

def directiva_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin':
            return redirect('/admin/')

        if group == 'residente':
            return redirect('user')

        if group == 'conserje':
            return redirect('conserje')
        
        if group == 'directiva':
            return view_func(request, *args, **kwargs)
    return wrapper_func