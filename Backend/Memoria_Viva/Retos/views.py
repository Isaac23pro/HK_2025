from django.shortcuts import render



from rest_framework import generics, permissions
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
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

class RetoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Reto.objects.all()
	serializer_class = RetoSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

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
