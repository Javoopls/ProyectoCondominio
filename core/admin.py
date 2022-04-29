from django.contrib import admin
from core.models import Espacio, Reserva, Condominio, Residente, GastosComunes

# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
    list_display = ["usuario", "espacio", "fecha", "horario", "fecha_creacion"]

class ResidenteAdmin(admin.ModelAdmin):
    list_display = ['user','rut', 'nro_vivienda', 'telefono']

class GcAdmin(admin.ModelAdmin):
    list_display = ['residente', 'month', 'monto']


admin.site.register(Espacio)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Condominio)
admin.site.register(Residente, ResidenteAdmin)
admin.site.register(GastosComunes, GcAdmin)