from django.contrib import admin

# Register your models here.

from .models import *


class ResidenteAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'vivienda', 'rut', 'telefono', 'moroso']

class ConserjeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'rut']

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id_reserva', 'residente', 'fecha_pago', 'pagada']

class PagoReservaAdmin(admin.ModelAdmin):
    list_display = ['residente', 'reserva', 'fecha_reserva', 'hora_reserva', 'fecha_creacion']

admin.site.register(Residente, ResidenteAdmin)
admin.site.register(Conserje, ConserjeAdmin)
admin.site.register(Espacio)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(CantReserva)
admin.site.register(PagoReserva, PagoReservaAdmin)
admin.site.register(Condominio)
admin.site.register(GastosComunes)
admin.site.register(Libro)
admin.site.register(PagoGC)
