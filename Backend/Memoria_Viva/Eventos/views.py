from django.shortcuts import render


from rest_framework import generics
from .models import Evento
from .serializers import EventoSerializer

# CRUD para Eventos
class EventoListCreateView(generics.ListCreateAPIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

class EventoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer
