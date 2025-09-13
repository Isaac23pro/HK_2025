from django.shortcuts import render


from rest_framework import generics
from .models import SaberPopular, ComentarioSaber, ReaccionSaber
from .serializers import SaberPopularSerializer, ComentarioSaberSerializer, ReaccionSaberSerializer

# CRUD para Saberes Populares
class SaberPopularListCreateView(generics.ListCreateAPIView):
	queryset = SaberPopular.objects.all()
	serializer_class = SaberPopularSerializer

class SaberPopularRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = SaberPopular.objects.all()
	serializer_class = SaberPopularSerializer

# CRUD para Comentarios de Saber
class ComentarioSaberListCreateView(generics.ListCreateAPIView):
	queryset = ComentarioSaber.objects.all()
	serializer_class = ComentarioSaberSerializer

class ComentarioSaberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ComentarioSaber.objects.all()
	serializer_class = ComentarioSaberSerializer

# CRUD para Reacciones de Saber
class ReaccionSaberListCreateView(generics.ListCreateAPIView):
	queryset = ReaccionSaber.objects.all()
	serializer_class = ReaccionSaberSerializer

class ReaccionSaberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReaccionSaber.objects.all()
	serializer_class = ReaccionSaberSerializer
