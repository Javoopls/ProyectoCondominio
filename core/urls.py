from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('carrito/', views.carrito, name="carrito"),
	path('pago/', views.pago, name="pago"),
	path('login_success/', views.login_success, name="login_success"), # Para hacer redirect login dinámico en función del rol
    path('user/', views.user, name="user"), # Page redirect residentes
	path('espacio/', views.espacio, name="espacio"),
]