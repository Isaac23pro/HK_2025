from django.shortcuts import render



from rest_framework import generics, permissions
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
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

class SaberPopularRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = SaberPopular.objects.all()
	serializer_class = SaberPopularSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

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
