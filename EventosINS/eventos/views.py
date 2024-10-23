# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from .models import Evento, Usuario
from datetime import datetime  # Para obtener la fecha actual
from django.urls import reverse

# Vista para el login
def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)

                # Verificar el rol del usuario y redirigir según corresponda
                if user.rol.nombre_rol == 'Administrador':
                    return redirect(reverse('admin_dashboard'))  # Redirige a la página del administrador
                elif user.rol.nombre_rol == 'Editor':
                    return redirect(reverse('editor_dashboard'))  # Redirige a la página del editor
                elif user.rol.nombre_rol == 'Usuario':
                    return redirect(reverse('user_dashboard'))  # Redirige a la página del usuario
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    
    return render(request, 'eventos/login.html', {'form': form})

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

# Vista para el dashboard del administrador
def admin_dashboard(request):
    return render(request, 'eventos/admin_dashboard.html')

# Vista para el dashboard del editor
def editor_dashboard(request):
    return render(request, 'eventos/editor_dashboard.html')

# Vista para el dashboard del usuario
def user_dashboard(request):
    return render(request, 'eventos/user_dashboard.html')
