# eventos/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import CustomLoginView, home, about_view    


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name='home'), #ruta para la pagina principal
    path('about/', about_view, name='about'),
]
