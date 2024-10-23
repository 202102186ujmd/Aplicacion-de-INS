import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventosINS.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from eventos.models import Usuario

# Cifrar contraseñas para usuarios existentes
usuarios = Usuario.objects.all()
for usuario in usuarios:
    if not usuario.password.startswith('pbkdf2_sha256$'):
        usuario.password = make_password(usuario.password)
        usuario.save()

print("Contraseñas cifradas correctamente.")
