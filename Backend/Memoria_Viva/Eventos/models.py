from django.db import models


from Usuarios.models import Usuario
from Catalogos.models import Localizacion, Categoria

# Modelo de Evento (calendario cultural)
class Evento(models.Model):
	nombre_evento = models.CharField(max_length=200)
	descripcion = models.TextField(null=True, blank=True)
	fecha_inicio = models.DateTimeField()
	fecha_fin = models.DateTimeField(null=True, blank=True)
	tipo_evento = models.CharField(max_length=60)  # Feria, Festividad, Tradición, etc.
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)
	localizacion = models.ForeignKey(Localizacion, null=True, blank=True, on_delete=models.SET_NULL)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
	latitud = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
	longitud = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombre_evento
