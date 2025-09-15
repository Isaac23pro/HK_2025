from django.shortcuts import render



from rest_framework import generics, permissions
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
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

class NotificacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Notificacion.objects.all()
	serializer_class = NotificacionSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
