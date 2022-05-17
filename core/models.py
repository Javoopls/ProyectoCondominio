from django.db import models
from django.contrib.auth.models import User

class Residente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vivienda = models.PositiveIntegerField()
    rut = models.CharField(max_length=20)
    telefono = models.IntegerField()
    moroso = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

class Conserje(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rut = models.CharField(max_length=20)
    
    def __str__(self):
        return self.rut

class Espacio(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.PositiveIntegerField(blank=True, null=True)
    aforo = models.PositiveIntegerField()
    descripcion = models.TextField(max_length=200)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    @property
    def imageURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url

class Reserva(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    pagada = models.BooleanField(default=False)
    id_reserva = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class CantReserva(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.SET_NULL, null=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class PagoReserva(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField()
    id_pago = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.residente

class Condominio(models.Model):
    nro_vivienda = models.IntegerField(verbose_name="Nro de Viviendas")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    def __str__(self):
        return self.nombre

class GastosComunes(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    monto = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.condominio
    
class Libro(models.Model):
    conserje = models.ForeignKey(Conserje, on_delete=models.CASCADE)
    
class PagoGC(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True)
    id_pago = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.id_pago
