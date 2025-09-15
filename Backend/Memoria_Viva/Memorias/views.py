from django.shortcuts import render



from rest_framework import generics, permissions
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import Memoria, Medio, ComentarioMemoria, ReaccionMemoria
from .serializers import MemoriaSerializer, MedioSerializer, ComentarioMemoriaSerializer, ReaccionMemoriaSerializer


# CRUD para Memorias
class MemoriaListCreateView(generics.ListCreateAPIView):
	queryset = Memoria.objects.all()
	serializer_class = MemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

	def perform_create(self, serializer):
		instance = serializer.save()
		logger.info(f"Memoria creada: {instance.titulo} por {self.request.user}")
		return instance

	def perform_update(self, serializer):
		instance = serializer.save()
		logger.info(f"Memoria editada: {instance.titulo} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Memoria eliminada: {instance.titulo} por {self.request.user}")
		return super().perform_destroy(instance)

	def perform_destroy(self, instance):
		logger.info(f"Memoria eliminada: {instance.titulo} por {self.request.user}")
		return super().perform_destroy(instance)

class MemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Memoria.objects.all()
	serializer_class = MemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
	def perform_update(self, serializer):
		instance = serializer.save()
		logger.info(f"Memoria editada: {instance.titulo} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Memoria eliminada: {instance.titulo} por {self.request.user}")
		return super().perform_destroy(instance)

# CRUD para Medios
class MedioListCreateView(generics.ListCreateAPIView):
	queryset = Medio.objects.all()
	serializer_class = MedioSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class MedioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Medio.objects.all()
	serializer_class = MedioSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

# CRUD para Comentarios de Memoria
class ComentarioMemoriaListCreateView(generics.ListCreateAPIView):
	queryset = ComentarioMemoria.objects.all()
	serializer_class = ComentarioMemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class ComentarioMemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ComentarioMemoria.objects.all()
	serializer_class = ComentarioMemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

# CRUD para Reacciones de Memoria
class ReaccionMemoriaListCreateView(generics.ListCreateAPIView):
	queryset = ReaccionMemoria.objects.all()
	serializer_class = ReaccionMemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class ReaccionMemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReaccionMemoria.objects.all()
	serializer_class = ReaccionMemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
