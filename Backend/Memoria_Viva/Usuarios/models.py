from django.db import models


from Catalogos.models import Rol, Localizacion

# Modelo de usuario extendido
class Usuario(models.Model):
	nombre = models.CharField(max_length=80)
	apellido = models.CharField(max_length=80, null=True, blank=True)
	nombre_usuario = models.CharField(max_length=50, unique=True)
	correo_electronico = models.EmailField(max_length=120, unique=True)
	contrasena_hash = models.CharField(max_length=255)
	rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
	tipo_usuario = models.CharField(max_length=20, null=True, blank=True, help_text="Estudiante, Docente, Familiar, Comunidad")
	institucion_educativa = models.CharField(max_length=200, null=True, blank=True)
	comunidad = models.CharField(max_length=150, null=True, blank=True)
	localizacion = models.ForeignKey(Localizacion, null=True, blank=True, on_delete=models.SET_NULL)
	fecha_registro = models.DateTimeField(auto_now_add=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre_usuario
