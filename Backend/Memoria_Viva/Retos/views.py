from django.shortcuts import render



from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import Reto, ProgresoReto, ReaccionReto
from .serializers import RetoSerializer, ProgresoRetoSerializer, ReaccionRetoSerializer


# CRUD para Retos

	queryset = Reto.objects.all()
	serializer_class = RetoSerializer

	@swagger_auto_schema(
		operation_description="Lista todos los retos o crea uno nuevo.",
		tags=["Retos"],
		request_body=RetoSerializer,
		responses={
			201: openapi.Response("Reto creado", RetoSerializer),
			400: "Datos inválidos o faltantes",
			401: "No autenticado"
		}
	)
	def post(self, request, *args, **kwargs):
		response = super().create(request, *args, **kwargs)
		if response.status_code == 201:
			logger.info(f"Reto creado: {response.data.get('titulo', '')} por {request.user}")
		return response

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

	def perform_create(self, serializer):
		instance = serializer.save()
		logger.info(f"Reto creado: {instance.titulo} por {self.request.user}")
		return instance

	def perform_update(self, serializer):
		instance = serializer.save()
		logger.info(f"Reto editado: {instance.titulo} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Reto eliminado: {instance.titulo} por {self.request.user}")
		return super().perform_destroy(instance)


	queryset = Reto.objects.all()
	serializer_class = RetoSerializer

	@swagger_auto_schema(
		operation_description="Obtiene el detalle de un reto por ID.",
		tags=["Retos"],
		responses={
			200: openapi.Response("Detalle de reto", RetoSerializer),
			404: "Reto no encontrado",
			401: "No autenticado"
		}
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_description="Actualiza un reto por ID.",
		tags=["Retos"],
		request_body=RetoSerializer,
		responses={
			200: openapi.Response("Reto actualizado", RetoSerializer),
			400: "Datos inválidos",
			404: "Reto no encontrado",
			401: "No autenticado"
		}
	)
	def put(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_description="Elimina un reto por ID.",
		tags=["Retos"],
		responses={
			204: "Reto eliminado",
			404: "Reto no encontrado",
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
		logger.info(f"Reto editado: {instance.titulo} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Reto eliminado: {instance.titulo} por {self.request.user}")
		return super().perform_destroy(instance)

# CRUD para Progreso en Retos
class ProgresoRetoListCreateView(generics.ListCreateAPIView):
	queryset = ProgresoReto.objects.all()
	serializer_class = ProgresoRetoSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class ProgresoRetoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ProgresoReto.objects.all()
	serializer_class = ProgresoRetoSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

# CRUD para Reacciones a Retos
class ReaccionRetoListCreateView(generics.ListCreateAPIView):
	queryset = ReaccionReto.objects.all()
	serializer_class = ReaccionRetoSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class ReaccionRetoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReaccionReto.objects.all()
	serializer_class = ReaccionRetoSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
