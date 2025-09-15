from django.shortcuts import render



from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import Memoria, Medio, ComentarioMemoria, ReaccionMemoria
from .serializers import MemoriaSerializer, MedioSerializer, ComentarioMemoriaSerializer, ReaccionMemoriaSerializer




# CRUD para Memorias
class MemoriaListCreateView(generics.ListCreateAPIView):
    queryset = Memoria.objects.all()
    serializer_class = MemoriaSerializer

    @swagger_auto_schema(
        operation_description="Lista todas las memorias o crea una nueva.",
        tags=["Memorias"],
        request_body=MemoriaSerializer,
        responses={
            201: openapi.Response("Memoria creada", MemoriaSerializer),
            400: "Datos inválidos o faltantes",
            401: "No autenticado"
        }
    )
    def post(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            logger.info(f"Memoria creada: {response.data.get('titulo', '')} por {request.user}")
        return response

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f"Memoria creada: {instance.titulo} por {self.request.user}")
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f"Memoria editada: {instance.titulo} por {self.request.user}")
        return instance

    def perform_destroy(self, instance):
        logger.info(f"Memoria eliminada: {instance.titulo} por {self.request.user}")
        return super().perform_destroy(instance)

class MemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memoria.objects.all()
    serializer_class = MemoriaSerializer


    class MemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Memoria.objects.all()
        serializer_class = MemoriaSerializer

        @swagger_auto_schema(
            operation_description="Obtiene el detalle de una memoria por ID.",
            tags=["Memorias"],
            responses={
                200: openapi.Response("Detalle de memoria", MemoriaSerializer),
                404: "Memoria no encontrada",
                401: "No autenticado"
            }
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_description="Actualiza una memoria por ID.",
            tags=["Memorias"],
            request_body=MemoriaSerializer,
            responses={
                200: openapi.Response("Memoria actualizada", MemoriaSerializer),
                400: "Datos inválidos",
                404: "Memoria no encontrada",
                401: "No autenticado"
            }
        )
        def put(self, request, *args, **kwargs):
            return super().update(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_description="Elimina una memoria por ID.",
            tags=["Memorias"],
            responses={
                204: "Memoria eliminada",
                404: "Memoria no encontrada",
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
            logger.info(f"Memoria editada: {instance.titulo} por {self.request.user}")
            return instance

        def perform_destroy(self, instance):
            logger.info(f"Memoria eliminada: {instance.titulo} por {self.request.user}")
            return super().perform_destroy(instance)

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class MedioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Medio.objects.all()
	serializer_class = MedioSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

# CRUD para Comentarios de Memoria
class ComentarioMemoriaListCreateView(generics.ListCreateAPIView):
	queryset = ComentarioMemoria.objects.all()
	serializer_class = ComentarioMemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class ComentarioMemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ComentarioMemoria.objects.all()
	serializer_class = ComentarioMemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

# CRUD para Reacciones de Memoria
class ReaccionMemoriaListCreateView(generics.ListCreateAPIView):
	queryset = ReaccionMemoria.objects.all()
	serializer_class = ReaccionMemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

class ReaccionMemoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReaccionMemoria.objects.all()
	serializer_class = ReaccionMemoriaSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
