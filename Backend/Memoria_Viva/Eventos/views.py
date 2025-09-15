from django.shortcuts import render



from rest_framework import generics, permissions
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
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

class EventoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
