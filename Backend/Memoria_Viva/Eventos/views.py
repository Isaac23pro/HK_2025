from django.shortcuts import render



from rest_framework import generics, permissions
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import Evento
from .serializers import EventoSerializer


# CRUD para Eventos
class EventoListCreateView(generics.ListCreateAPIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

	def perform_create(self, serializer):
		instance = serializer.save()
		logger.info(f"Evento creado: {instance.nombre_evento} por {self.request.user}")
		return instance

	def perform_update(self, serializer):
		instance = serializer.save()
		logger.info(f"Evento editado: {instance.nombre_evento} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Evento eliminado: {instance.nombre_evento} por {self.request.user}")
		return super().perform_destroy(instance)

	def perform_create(self, serializer):
		instance = serializer.save()
		logger.info(f"Evento creado: {instance.nombre_evento} por {self.request.user}")
		return instance

	def perform_update(self, serializer):
		instance = serializer.save()
		logger.info(f"Evento editado: {instance.nombre_evento} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Evento eliminado: {instance.nombre_evento} por {self.request.user}")
		return super().perform_destroy(instance)

class EventoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
	def perform_update(self, serializer):
		instance = serializer.save()
		logger.info(f"Evento editado: {instance.nombre_evento} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Evento eliminado: {instance.nombre_evento} por {self.request.user}")
		return super().perform_destroy(instance)
