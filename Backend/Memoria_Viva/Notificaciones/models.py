from django.db import models


from Usuarios.models import Usuario

# Modelo de Notificación
class Notificacion(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=50)  # 'NuevoComentario','Aprobacion','NuevoEvento', etc.
	mensaje = models.CharField(max_length=600)
	enlace = models.CharField(max_length=600, null=True, blank=True)
	leida = models.BooleanField(default=False)
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.tipo} para {self.usuario}"
