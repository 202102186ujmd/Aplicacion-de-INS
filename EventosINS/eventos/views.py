# eventos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Event
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .forms import CustomSetPasswordForm  # Asegúrate de haber importado el formulario personalizado

# Página principal (Home)
def home(request):
    # Mostrar solo los eventos públicos
    eventos = Event.objects.filter(is_public=True)
    return render(request, 'eventos/index.html', {'eventos': eventos})

# Vista para el dashboard del administrador
def admin_dashboard(request):
    return render(request, 'eventos/admin_dashboard.html')


# Vista personalizada de Login
class CustomLoginView(LoginView):
    template_name = 'eventos/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('admin_dashboard')  # Ajuste con reverse_lazy

    def form_valid(self, form):
        return super().form_valid(form)

# Registro de usuario
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Tu cuenta ha sido creada y has iniciado sesión.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Detalle del evento
@login_required
def event_detail(request, id):
    evento = get_object_or_404(Event, id=id)
    return render(request, 'evento_detail.html', {'evento': evento})

# Vistas personalizadas para recuperación de contraseña con plantilla de correo en HTML
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.txt'  # Plantilla de texto plano para el correo
    html_email_template_name = 'registration/password_reset_email.html'  # Plantilla HTML para el correo
    success_url = reverse_lazy('password_reset_done')
    
    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        subject = render_to_string(subject_template_name, context).strip()
        body = render_to_string(email_template_name, context).strip()

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name:
            html_email = render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, "text/html")
        email_message.send()


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = CustomSetPasswordForm  # Utiliza el formulario personalizado para añadir estilos
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'


def about(request):
    return render(request, 'eventos/about.html')
