# eventos/views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .forms import LoginForm
from .models import Evento

# Vista para el login
class CustomLoginView(LoginView):
    template_name = 'eventos/login.html'  # Asegúrate de que este sea el archivo correcto
    authentication_form = LoginForm

# Vista para la página principal
def home(request):
    eventos = Evento.objects.filter(estado='activo')  # Obtener solo eventos activos
    return render(request, 'eventos/home.html', {'eventos': eventos}) 

# Vista para la pagina de about
def about_view(request):
    return render(request, 'eventos/about.html') 



