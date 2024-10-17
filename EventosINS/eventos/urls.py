# eventos/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import CustomLoginView, home, about_view, evento_detail    


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name='home'), #ruta para la pagina principal
    path('about/', about_view, name='about'),
   path('evento/<int:id_evento>/', evento_detail, name='evento_detail'), 
]
