from django.shortcuts import render



from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import Evento
from .serializers import EventoSerializer


# CRUD para Eventos
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

	@swagger_auto_schema(
		operation_description="Lista todos los eventos o crea uno nuevo.",
		tags=["Eventos"],
		request_body=EventoSerializer,
		responses={
			201: openapi.Response("Evento creado", EventoSerializer),
			400: "Datos inválidos o faltantes",
			401: "No autenticado"
		}
	)
	def post(self, request, *args, **kwargs):
		response = super().create(request, *args, **kwargs)
		if response.status_code == 201:
			logger.info(f"Evento creado: {response.data.get('nombre_evento', '')} por {request.user}")
		return response

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

	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

	@swagger_auto_schema(
		operation_description="Obtiene el detalle de un evento por ID.",
		tags=["Eventos"],
		responses={
			200: openapi.Response("Detalle de evento", EventoSerializer),
			404: "Evento no encontrado",
			401: "No autenticado"
		}
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_description="Actualiza un evento por ID.",
		tags=["Eventos"],
		request_body=EventoSerializer,
		responses={
			200: openapi.Response("Evento actualizado", EventoSerializer),
			400: "Datos inválidos",
			404: "Evento no encontrado",
			401: "No autenticado"
		}
	)
	def put(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_description="Elimina un evento por ID.",
		tags=["Eventos"],
		responses={
			204: "Evento eliminado",
			404: "Evento no encontrado",
			401: "No autenticado"
		}
	)
	def delete(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)

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

	def perform_destroy(self, instance):
		logger.info(f"Evento eliminado: {instance.nombre_evento} por {self.request.user}")
		return super().perform_destroy(instance)
