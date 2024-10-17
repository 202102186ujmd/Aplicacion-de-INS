# Importaciones necesarias
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from .forms import LoginForm
from .models import Evento
from datetime import datetime  # Para obtener la fecha actual

# Vista para el login
class CustomLoginView(LoginView):
    template_name = 'eventos/login.html'
    authentication_form = LoginForm

# Vista para la página principal
def home(request):
    # Obtener la fecha actual
    now = datetime.now()

    # Filtrar eventos que ocurren en el mes actual y con privacidad específica
    eventos = Evento.objects.filter(
        fecha__year=now.year,
        fecha__month=now.month,
        privacidad='publico',  # Cambia 'publico' por el valor de privacidad que desees
        estado='activo'  # Asumiendo que solo mostramos eventos activos
    )

    return render(request, 'eventos/home.html', {'eventos': eventos})

# Vista para la página de about
def about_view(request):
    return render(request, 'eventos/about.html')

# Vista para los detalles del evento
def evento_detail(request, id_evento):
    # Obtener el evento o mostrar un error 404 si no existe
    evento = get_object_or_404(Evento, id_evento=id_evento)

    # Renderizar la plantilla 'evento_detail.html' con los detalles del evento
    return render(request, 'eventos/evento_detail.html', {'evento': evento})