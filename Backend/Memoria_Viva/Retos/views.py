from django.shortcuts import render



from rest_framework import generics, permissions
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import Reto, ProgresoReto, ReaccionReto
from .serializers import RetoSerializer, ProgresoRetoSerializer, ReaccionRetoSerializer


# CRUD para Retos
class RetoListCreateView(generics.ListCreateAPIView):
    queryset = Reto.objects.all()
    serializer_class = RetoSerializer

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

class RetoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Reto.objects.all()
	serializer_class = RetoSerializer

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
