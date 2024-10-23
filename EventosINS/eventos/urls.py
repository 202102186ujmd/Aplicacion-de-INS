# eventos/urls.py
from django.urls import path
from .views import home, about_view, evento_detail, custom_login, admin_dashboard, editor_dashboard, user_dashboard

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('', home, name='home'),
    path('about/', about_view, name='about'),
    path('evento/<int:id_evento>/', evento_detail, name='evento_detail'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('editor/dashboard/', editor_dashboard, name='editor_dashboard'),
    path('user/dashboard/', user_dashboard, name='user_dashboard'),
]
