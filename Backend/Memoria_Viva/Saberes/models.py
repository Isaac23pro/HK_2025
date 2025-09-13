from django.db import models


from Usuarios.models import Usuario
from Catalogos.models import Localizacion, Categoria

# Modelo de Saber Popular
class SaberPopular(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.TextField(null=True, blank=True)
	tipo_saber = models.CharField(max_length=50)  # Receta, Costumbre, Leyenda, Artesanía, etc.
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	localizacion = models.ForeignKey(Localizacion, null=True, blank=True, on_delete=models.SET_NULL)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
	estado = models.CharField(max_length=12, default='Pendiente')  # Pendiente, Aprobado, Rechazado
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	aprobado_por = models.ForeignKey(Usuario, null=True, blank=True, related_name='saberes_aprobados', on_delete=models.SET_NULL)
	fecha_aprobacion = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.titulo

# Modelo de comentario en saber
class ComentarioSaber(models.Model):
	saber = models.ForeignKey(SaberPopular, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	comentario = models.CharField(max_length=600)
	fecha_comentario = models.DateTimeField(auto_now_add=True)
	estado = models.CharField(max_length=10, default='Activo')  # Activo, Eliminado

	def __str__(self):
		return f"Comentario de {self.usuario} en {self.saber}"

# Modelo de reacción en saber
class ReaccionSaber(models.Model):
	saber = models.ForeignKey(SaberPopular, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	tipo_reaccion = models.CharField(max_length=20, default='Like')  # Like, Corazon, Aplauso
	fecha_reaccion = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('saber', 'usuario')

	def __str__(self):
		return f"{self.tipo_reaccion} de {self.usuario} en {self.saber}"
