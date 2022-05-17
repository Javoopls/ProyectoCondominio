from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Residente)
admin.site.register(Conserje)
admin.site.register(Espacio)
admin.site.register(Reserva)
admin.site.register(CantReserva)
admin.site.register(PagoReserva)
admin.site.register(Condominio)
admin.site.register(GastosComunes)
admin.site.register(Libro)
admin.site.register(PagoGC)
