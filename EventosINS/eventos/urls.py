from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from eventos import views  # Importa las vistas desde la app 'eventos'

urlpatterns = [
    # Ruta para la administración de Django
    path('admin/', admin.site.urls),

    # Ruta para la página principal (home)
    path('', views.home, name='home'),  # Página de inicio pública

    # Rutas para la autenticación (login, logout, registro)
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Rutas para la recuperación de contraseña con las nuevas plantillas en 'registration/'
    path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # Ruta para ver detalles de un evento (requiere autenticación)
    path('event/<int:id>/', views.event_detail, name='evento_detail'),
    
    # Página "Acerca de"
    path('about/', views.about, name='about'),  
]
