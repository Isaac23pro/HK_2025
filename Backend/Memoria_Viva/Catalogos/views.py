from django.shortcuts import render


from rest_framework import generics
from .models import Rol, Localizacion, Categoria
from .serializers import RolSerializer, LocalizacionSerializer, CategoriaSerializer

# CRUD para Roles
class RolListCreateView(generics.ListCreateAPIView):
	queryset = Rol.objects.all()
	serializer_class = RolSerializer

class RolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Rol.objects.all()
	serializer_class = RolSerializer

# CRUD para Localizaciones
class LocalizacionListCreateView(generics.ListCreateAPIView):
	queryset = Localizacion.objects.all()
	serializer_class = LocalizacionSerializer

class LocalizacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Localizacion.objects.all()
	serializer_class = LocalizacionSerializer

# CRUD para Categorias
class CategoriaListCreateView(generics.ListCreateAPIView):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer
