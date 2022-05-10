
from django.urls import path
from .views import disponibilidad, home,\
    login_success, user,\
        espacios, disponibilidad, cart,\
            conserjeView

# Urls del Core

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),

    path('login_success', login_success, name="login_success"), # Para hacer redirect login dinámico en función del rol
    path('user/', user, name="user"), # Page redirect residentes


    # Reservas
    path('espacios/', espacios, name="espacios"),
    # path('disponibilidad/', disponibilidad, name="disponibilidad"),
    path('disponibilidad/<id>', disponibilidad, name="disponibilidad"),
    path('cart/', cart, name="cart"),
    # path('cart/<hr>', cart, name="cart"),

    # Conserje
    path('conserjeria/', conserjeView, name="conserjeria")
]