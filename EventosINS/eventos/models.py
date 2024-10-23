from django.db import models

# Modelo para la tabla de roles
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.nombre_rol

# Modelo para la tabla de usuarios
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre_usuario

# Modelo de la tabla eventos
class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)  # Usa 'id_evento' como clave primaria
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])
    privacidad = models.CharField(max_length=50)
    id_usuario_creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario_creador')

    class Meta:
        db_table = 'eventos'

    def __str__(self):
        return self.titulo
