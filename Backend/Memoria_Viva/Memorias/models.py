from django.db import models


from Usuarios.models import Usuario
from Catalogos.models import Localizacion, Rol
from Catalogos.models import Categoria  # Este modelo se agregará en Catalogos

# Modelo de Memoria (relato comunitario)
class Memoria(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField(null=True, blank=True)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	localizacion = models.ForeignKey(Localizacion, null=True, blank=True, on_delete=models.SET_NULL)
	categoria = models.ForeignKey('Catalogos.Categoria', null=True, blank=True, on_delete=models.SET_NULL)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	estado = models.CharField(max_length=12, default='Pendiente')  # Pendiente, Aprobado, Rechazado
	aprobado_por = models.ForeignKey(Usuario, null=True, blank=True, related_name='memorias_aprobadas', on_delete=models.SET_NULL)
	fecha_aprobacion = models.DateTimeField(null=True, blank=True)
	es_publico = models.BooleanField(default=False)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo

# Modelo de Medio asociado a una memoria (imagen, audio, video, texto)
class Medio(models.Model):
	memoria = models.ForeignKey(Memoria, on_delete=models.CASCADE)
	tipo_medio = models.CharField(max_length=20)  # Imagen, Audio, Video, Texto
	url_archivo = models.CharField(max_length=1000, null=True, blank=True)
	contenido_texto = models.TextField(null=True, blank=True)
	fecha_carga = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.tipo_medio} - {self.memoria.titulo}"

# Modelo de comentario en memoria
class ComentarioMemoria(models.Model):
	memoria = models.ForeignKey(Memoria, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	comentario = models.CharField(max_length=600)
	fecha_comentario = models.DateTimeField(auto_now_add=True)
	estado = models.CharField(max_length=10, default='Activo')  # Activo, Eliminado

	def __str__(self):
		return f"Comentario de {self.usuario} en {self.memoria}"

# Modelo de reacción en memoria
class ReaccionMemoria(models.Model):
	memoria = models.ForeignKey(Memoria, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	tipo_reaccion = models.CharField(max_length=20, default='Like')  # Like, Corazon, Aplauso
	fecha_reaccion = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('memoria', 'usuario')

	def __str__(self):
		return f"{self.tipo_reaccion} de {self.usuario} en {self.memoria}"
