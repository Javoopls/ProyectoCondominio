from random import choices
from tabnanny import verbose
from xml.etree.ElementTree import tostring
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
import calendar

# MONTH_CHOICES = (
#     ("1", "Enero"), 
#     ("2", "Febrero"), 
#     ("3", "Marzo"), 
#     ("4", "Abril"), 
#     ("5", "Mayo"), 
#     ("6", "Junio"), 
#     ("7", "Julio"), 
#     ("8", "Agosto"), 
#     ("9", "Septiembre"), 
#     ("10", "Octubre"), 
#     ("11", "Noviembre"), 
#     ("12", "Diciembre"), 
# )

class Espacio(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="Nombre")
    precio = models.IntegerField(blank=True, null=True, verbose_name="Precio")
    aforo = models.IntegerField()
    temporada = models.BooleanField()
    descripcion = models.TextField(max_length=200, verbose_name="Descripción")
    imagen = models.ImageField(upload_to = "espacios", null=True)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Creación Registro")
    fecha = models.DateField(verbose_name="Fecha")
    horario = models.CharField(max_length=20, verbose_name="Horario")

    def __str__(self):
        return self.usuario.first_name

WEEKDAY_CHOICES = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
)
class ReservasHorario(models.Model):
    day = models.CharField(max_length= 9,choices=WEEKDAY_CHOICES, verbose_name='Día')
    inicio = models.TimeField(verbose_name="Inicio")
    termino = models.TimeField(verbose_name="Término")
    def __str__(self):
        cadena = self.day + ': ' + str(self.inicio) + ' - ' + str(self.termino)
        return cadena

class Residente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nro_vivienda = models.CharField(max_length=5, verbose_name="Nro Vivienda")
    rut = models.CharField(max_length=20, verbose_name="Rut")
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.user.first_name

class Condominio(models.Model):
    nro_vivienda = models.IntegerField(verbose_name="Nro de Viviendas")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    def __str__(self):
        return self.nombre

class GastosComunes(models.Model):
    # residente = models.ForeignKey(Residente.__name__, on_delete=models.CASCADE)
    # nro_vivienda = models.ForeignKey(Residente, on_delete=models.CASCADE)
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    monto = models.IntegerField(blank=True, null=True, verbose_name="Monto")
    class Meta:
        verbose_name_plural = "Gastos Comunes"
    def __str__(self):
        return 'Vivienda ' + self.residente.nro_vivienda