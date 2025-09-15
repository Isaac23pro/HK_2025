from django.shortcuts import render



from rest_framework import generics, permissions
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import SaberPopular, ComentarioSaber, ReaccionSaber
from .serializers import SaberPopularSerializer, ComentarioSaberSerializer, ReaccionSaberSerializer


# CRUD para Saberes Populares
class SaberPopularListCreateView(generics.ListCreateAPIView):
    queryset = SaberPopular.objects.all()
    serializer_class = SaberPopularSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f"Saber creado: {instance.titulo} por {self.request.user}")
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f"Saber editado: {instance.titulo} por {self.request.user}")
        return instance

    def perform_destroy(self, instance):
        logger.info(f"Saber eliminado: {instance.titulo} por {self.request.user}")
        return super().perform_destroy(instance)

class SaberPopularRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = SaberPopular.objects.all()
	serializer_class = SaberPopularSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
	def perform_update(self, serializer):
		instance = serializer.save()
		logger.info(f"Saber editado: {instance.titulo} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Saber eliminado: {instance.titulo} por {self.request.user}")
		return super().perform_destroy(instance)

# CRUD para Comentarios de Saber
class ComentarioSaberListCreateView(generics.ListCreateAPIView):
	queryset = ComentarioSaber.objects.all()
	serializer_class = ComentarioSaberSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class ComentarioSaberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ComentarioSaber.objects.all()
	serializer_class = ComentarioSaberSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

# CRUD para Reacciones de Saber
class ReaccionSaberListCreateView(generics.ListCreateAPIView):
	queryset = ReaccionSaber.objects.all()
	serializer_class = ReaccionSaberSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class ReaccionSaberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReaccionSaber.objects.all()
	serializer_class = ReaccionSaberSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
