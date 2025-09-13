from django.db import models


from Usuarios.models import Usuario

# Modelo de Reto Didáctico
class Reto(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField(null=True, blank=True)
	preguntas = models.TextField(help_text="JSON con preguntas y respuestas")
	tema = models.CharField(max_length=80)
	nivel_dificultad = models.CharField(max_length=10, default='Medio')  # Facil, Medio, Dificil
	puntos_base = models.IntegerField(default=10)
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo

# Modelo de Progreso en Retos
class ProgresoReto(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	reto = models.ForeignKey(Reto, on_delete=models.CASCADE)
	puntos_obtenidos = models.IntegerField()
	tiempo_segundos = models.IntegerField(null=True, blank=True)
	fecha_completado = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('usuario', 'reto')

	def __str__(self):
		return f"{self.usuario} - {self.reto}"

# Modelo de Reacción a Reto
class ReaccionReto(models.Model):
	reto = models.ForeignKey(Reto, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	tipo_reaccion = models.CharField(max_length=20, default='Like')  # Like, Corazon, Aplauso
	fecha_reaccion = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('reto', 'usuario')

	def __str__(self):
		return f"{self.tipo_reaccion} de {self.usuario} en {self.reto}"
