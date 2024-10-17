from django.db import models

#Modelo de la tabla eventos
class Evento(models.Model):
    id_evento = models.IntegerField(primary_key=True)  # Usa 'id_evento' como clave primaria
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])
    privacidad = models.CharField(max_length=50)
    id_usuario_creador = models.IntegerField()

    class Meta:
        db_table = 'eventos'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.titulo
