from django.shortcuts import render


from rest_framework import generics
from .models import Notificacion
from .serializers import NotificacionSerializer

# CRUD para Notificaciones
class NotificacionListCreateView(generics.ListCreateAPIView):
	queryset = Notificacion.objects.all()
	serializer_class = NotificacionSerializer

class NotificacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Notificacion.objects.all()
	serializer_class = NotificacionSerializer
