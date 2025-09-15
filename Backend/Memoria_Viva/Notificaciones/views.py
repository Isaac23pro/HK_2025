from django.shortcuts import render



from rest_framework import generics, permissions
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import Notificacion
from .serializers import NotificacionSerializer


# CRUD para Notificaciones
class NotificacionListCreateView(generics.ListCreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f"Notificación creada para usuario {instance.usuario} por {self.request.user}")
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f"Notificación editada para usuario {instance.usuario} por {self.request.user}")
        return instance

    def perform_destroy(self, instance):
        logger.info(f"Notificación eliminada para usuario {instance.usuario} por {self.request.user}")
        return super().perform_destroy(instance)

class NotificacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Notificacion.objects.all()
	serializer_class = NotificacionSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
	def perform_update(self, serializer):
		instance = serializer.save()
		logger.info(f"Notificación editada para usuario {instance.usuario} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Notificación eliminada para usuario {instance.usuario} por {self.request.user}")
		return super().perform_destroy(instance)
