from django.shortcuts import render



from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import SaberPopular, ComentarioSaber, ReaccionSaber
from .serializers import SaberPopularSerializer, ComentarioSaberSerializer, ReaccionSaberSerializer




# CRUD para Saberes Populares
class SaberPopularListCreateView(generics.ListCreateAPIView):
    queryset = SaberPopular.objects.all()
    serializer_class = SaberPopularSerializer

    @swagger_auto_schema(
        operation_description="Lista todos los saberes populares o crea uno nuevo.",
        tags=["Saberes"],
        request_body=SaberPopularSerializer,
        responses={
            201: openapi.Response("Saber creado", SaberPopularSerializer),
            400: "Datos inválidos o faltantes",
            401: "No autenticado"
        }
    )
    def post(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            logger.info(f"Saber creado: {response.data.get('titulo', '')} por {request.user}")
        return response

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f"Saber creado: {instance.titulo} por {self.request.user}")
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f"Saber editado: {instance.titulo} por {self.request.user}")
        return instance

    def perform_destroy(self, instance):
        logger.info(f"Saber eliminado: {instance.titulo} por {self.request.user}")
        return super().perform_destroy(instance)


class SaberPopularRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaberPopular.objects.all()
    serializer_class = SaberPopularSerializer

    @swagger_auto_schema(
        operation_description="Obtiene el detalle de un saber popular por ID.",
        tags=["Saberes"],
        responses={
            200: openapi.Response("Detalle de saber popular", SaberPopularSerializer),
            404: "Saber no encontrado",
            401: "No autenticado"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualiza un saber popular por ID.",
        tags=["Saberes"],
        request_body=SaberPopularSerializer,
        responses={
            200: openapi.Response("Saber actualizado", SaberPopularSerializer),
            400: "Datos inválidos",
            404: "Saber no encontrado",
            401: "No autenticado"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Elimina un saber popular por ID.",
        tags=["Saberes"],
        responses={
            204: "Saber eliminado",
            404: "Saber no encontrado",
            401: "No autenticado"
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f"Saber editado: {instance.titulo} por {self.request.user}")
        return instance

    def perform_destroy(self, instance):
        logger.info(f"Saber eliminado: {instance.titulo} por {self.request.user}")
        return super().perform_destroy(instance)

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
