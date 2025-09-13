from django.shortcuts import render


from rest_framework import generics
from .models import Reto, ProgresoReto, ReaccionReto
from .serializers import RetoSerializer, ProgresoRetoSerializer, ReaccionRetoSerializer

# CRUD para Retos
class RetoListCreateView(generics.ListCreateAPIView):
	queryset = Reto.objects.all()
	serializer_class = RetoSerializer

class RetoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Reto.objects.all()
	serializer_class = RetoSerializer

# CRUD para Progreso en Retos
class ProgresoRetoListCreateView(generics.ListCreateAPIView):
	queryset = ProgresoReto.objects.all()
	serializer_class = ProgresoRetoSerializer

class ProgresoRetoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ProgresoReto.objects.all()
	serializer_class = ProgresoRetoSerializer

# CRUD para Reacciones a Retos
class ReaccionRetoListCreateView(generics.ListCreateAPIView):
	queryset = ReaccionReto.objects.all()
	serializer_class = ReaccionRetoSerializer

class ReaccionRetoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReaccionReto.objects.all()
	serializer_class = ReaccionRetoSerializer
