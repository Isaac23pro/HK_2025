
from django.db import models

# Modelo para categorías genéricas (Memoria, Saber, Evento)
class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=400, null=True, blank=True)
	tipo = models.CharField(max_length=30, help_text="Memoria, Saber, Evento")

	class Meta:
		unique_together = ('nombre', 'tipo')

	def __str__(self):
		return f"{self.nombre} ({self.tipo})"


# Modelo para roles de usuario (Administrador, Moderador, Estudiante, etc.)
class Rol(models.Model):
	nombre = models.CharField(max_length=40, unique=True, help_text="Nombre del rol, ej: Administrador")
	es_interno = models.BooleanField(default=False, help_text="Indica si el rol es interno (admin/moderador)")

	def __str__(self):
		return self.nombre

# Modelo para localizaciones (país, departamento, municipio, barrio, geolocalización)
class Localizacion(models.Model):
	pais = models.CharField(max_length=60, default="Nicaragua")
	departamento = models.CharField(max_length=100, null=True, blank=True)
	municipio = models.CharField(max_length=100, null=True, blank=True)
	barrio = models.CharField(max_length=120, null=True, blank=True)
	latitud = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
	longitud = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)

	def __str__(self):
		return f"{self.pais} - {self.departamento or ''} - {self.municipio or ''} - {self.barrio or ''}"
