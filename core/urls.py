from django.urls import path
from .views import home,\
    login_success, user,\
        espacios, disponibilidad

# Urls del Core

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),

    path('login_success', login_success, name="login_success"), # Para hacer redirect login dinámico en función del rol
    path('user/', user, name="user"), # Page redirect residentes

    # Reservas
    path('espacios/', espacios, name="espacios"),
    path('disponibilidad/', disponibilidad, name="disponibilidad"),
]