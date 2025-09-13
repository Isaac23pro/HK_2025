from django.shortcuts import render


from rest_framework import generics
from .models import Memoria, Medio, ComentarioMemoria, ReaccionMemoria
from .serializers import MemoriaSerializer, MedioSerializer, ComentarioMemoriaSerializer, ReaccionMemoriaSerializer

# CRUD para Memorias
class MemoriaListCreateView(generics.ListCreateAPIView):
	queryset = Memoria.objects.all()
	serializer_class = MemoriaSerializer

class MemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Memoria.objects.all()
	serializer_class = MemoriaSerializer

# CRUD para Medios
class MedioListCreateView(generics.ListCreateAPIView):
	queryset = Medio.objects.all()
	serializer_class = MedioSerializer

class MedioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Medio.objects.all()
	serializer_class = MedioSerializer

# CRUD para Comentarios de Memoria
class ComentarioMemoriaListCreateView(generics.ListCreateAPIView):
	queryset = ComentarioMemoria.objects.all()
	serializer_class = ComentarioMemoriaSerializer

class ComentarioMemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ComentarioMemoria.objects.all()
	serializer_class = ComentarioMemoriaSerializer

# CRUD para Reacciones de Memoria
class ReaccionMemoriaListCreateView(generics.ListCreateAPIView):
	queryset = ReaccionMemoria.objects.all()
	serializer_class = ReaccionMemoriaSerializer

class ReaccionMemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReaccionMemoria.objects.all()
	serializer_class = ReaccionMemoriaSerializer
