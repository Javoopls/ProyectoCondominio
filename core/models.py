from turtle import back
from django.db import models
from django.contrib.auth.models import User

class Residente(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
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
    reservado = models.BooleanField(default=False, null=True, blank=True)
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
    fecha_pago = models.DateTimeField(auto_now_add=True)
    pagada = models.BooleanField(default=False)
    id_reserva = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def reservar(self):
        reservar = False
        cantreserva = self.cantreserva_set.all()
        for i in cantreserva:
            if i.espacio.reservado == False:
                reservar = True
        return reservar

    @property
    def obtener_total_carrito(self):
        cantreserva = self.cantreserva_set.all()
        total = sum([espacio.obtener_total for espacio in cantreserva])
        return total

    @property
    def obtener_total_espacios(self):
        cantreserva = self.cantreserva_set.all()
        total = sum([espacio.cantidad for espacio in cantreserva])
        return total

class CantReserva(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.SET_NULL, null=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    @property
    def obtener_total(self):
        total = self.espacio.precio
        return total

class PagoReserva(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE, null=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, null=True)
    fecha_reserva = models.DateField(null=True)
    hora_reserva = models.TimeField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.fecha_reserva

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
