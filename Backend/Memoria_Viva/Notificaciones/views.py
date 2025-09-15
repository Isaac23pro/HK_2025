from django.shortcuts import render



from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from Usuarios.permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from Memoria_Viva.logging_config import logger
from .models import Notificacion
from .serializers import NotificacionSerializer


# CRUD para Notificaciones
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    class NotificacionListCreateView(generics.ListCreateAPIView):
        queryset = Notificacion.objects.all()
        serializer_class = NotificacionSerializer

    @swagger_auto_schema(
        operation_description="Lista todas las notificaciones o crea una nueva.",
        tags=["Notificaciones"],
        request_body=NotificacionSerializer,
        responses={
            201: openapi.Response("Notificación creada", NotificacionSerializer),
            400: "Datos inválidos o faltantes",
            401: "No autenticado"
        }
    )
    def post(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            logger.info(f"Notificación creada para usuario {response.data.get('usuario', '')} por {request.user}")
        return response

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f"Notificación creada para usuario {instance.usuario} por {self.request.user}")
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f"Notificación editada para usuario {instance.usuario} por {self.request.user}")
        return instance

    def perform_destroy(self, instance):
        logger.info(f"Notificación eliminada para usuario {instance.usuario} por {self.request.user}")
        return super().perform_destroy(instance)

    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    class NotificacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Notificacion.objects.all()
        serializer_class = NotificacionSerializer

    @swagger_auto_schema(
        operation_description="Obtiene el detalle de una notificación por ID.",
        tags=["Notificaciones"],
        responses={
            200: openapi.Response("Detalle de notificación", NotificacionSerializer),
            404: "Notificación no encontrada",
            401: "No autenticado"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualiza una notificación por ID.",
        tags=["Notificaciones"],
        request_body=NotificacionSerializer,
        responses={
            200: openapi.Response("Notificación actualizada", NotificacionSerializer),
            400: "Datos inválidos",
            404: "Notificación no encontrada",
            401: "No autenticado"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Elimina una notificación por ID.",
        tags=["Notificaciones"],
        responses={
            204: "Notificación eliminada",
            404: "Notificación no encontrada",
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
        logger.info(f"Notificación editada para usuario {instance.usuario} por {self.request.user}")
        return instance

    def perform_destroy(self, instance):
        logger.info(f"Notificación eliminada para usuario {instance.usuario} por {self.request.user}")
        return super().perform_destroy(instance)
