from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status as drf_status
# Endpoint para login de usuario
class LoginView(APIView):
	permission_classes = [AllowAny]

	def post(self, request):
		nombre_usuario = request.data.get('nombre_usuario')
		contrasena = request.data.get('contrasena')
		# NOTA: Aquí deberías usar un sistema de hash seguro y comparar hashes
		usuario = Usuario.objects.filter(nombre_usuario=nombre_usuario, contrasena_hash=contrasena, activo=True).first()
		if usuario:
			# En un sistema real, usarías Django User y Token, aquí es solo ejemplo
			return Response({'mensaje': 'Login exitoso', 'usuario_id': usuario.id}, status=drf_status.HTTP_200_OK)
		return Response({'error': 'Credenciales inválidas'}, status=drf_status.HTTP_401_UNAUTHORIZED)

# Endpoint para logout (dummy, solo para estructura)
class LogoutView(APIView):
	def post(self, request):
		# Aquí podrías eliminar el token o hacer logout real si usas autenticación con tokens
		return Response({'mensaje': 'Logout exitoso'}, status=drf_status.HTTP_200_OK)
from django.shortcuts import render



from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
from Memoria_Viva.logging_config import logger


# Vista para listar y crear usuarios
# NOTA: Para lógica avanzada de permisos por rol, usar IsAdmin, IsModerator, IsOwnerOrReadOnly
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

	@swagger_auto_schema(
		operation_description="Lista todos los usuarios o crea uno nuevo.",
		tags=["Usuarios"],
		request_body=openapi.Schema(
			type=openapi.TYPE_OBJECT,
			required=["nombre", "nombre_usuario", "correo_electronico", "contrasena_hash", "rol_id"],
			properties={
				"nombre": openapi.Schema(type=openapi.TYPE_STRING, example="Juan"),
				"apellido": openapi.Schema(type=openapi.TYPE_STRING, example="Pérez"),
				"nombre_usuario": openapi.Schema(type=openapi.TYPE_STRING, example="juanperez"),
				"correo_electronico": openapi.Schema(type=openapi.TYPE_STRING, example="juan@mail.com"),
				"contrasena_hash": openapi.Schema(type=openapi.TYPE_STRING, example="hash123456"),
				"rol_id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
			},
		),
		responses={
			201: openapi.Response("Usuario creado", UsuarioSerializer),
			400: "Datos inválidos o faltantes",
			401: "No autenticado"
		}
	)
	def post(self, request, *args, **kwargs):
		"""
		Crea un nuevo usuario. El password debe venir hasheado desde el frontend por seguridad.
		"""
		response = super().create(request, *args, **kwargs)
		if response.status_code == 201:
			logger.info(f"Usuario creado: {response.data.get('nombre_usuario', '')} por {request.user}")
		return response

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]

# Vista para obtener, actualizar o eliminar un usuario específico
# NOTA: Para lógica avanzada de permisos por rol, usar IsAdmin, IsModerator, IsOwnerOrReadOnly
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

	@swagger_auto_schema(
		operation_description="Obtiene el detalle de un usuario por ID.",
		tags=["Usuarios"],
		responses={
			200: openapi.Response("Detalle de usuario", UsuarioSerializer),
			404: "Usuario no encontrado",
			401: "No autenticado"
		}
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_description="Actualiza un usuario por ID.",
		tags=["Usuarios"],
		request_body=UsuarioSerializer,
		responses={
			200: openapi.Response("Usuario actualizado", UsuarioSerializer),
			400: "Datos inválidos",
			404: "Usuario no encontrado",
			401: "No autenticado"
		}
	)
	def put(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_description="Elimina un usuario por ID.",
		tags=["Usuarios"],
		responses={
			204: "Usuario eliminado",
			404: "Usuario no encontrado",
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
		logger.info(f"Usuario editado: {instance.nombre_usuario} por {self.request.user}")
		return instance

	def perform_destroy(self, instance):
		logger.info(f"Usuario eliminado: {instance.nombre_usuario} por {self.request.user}")
		return super().perform_destroy(instance)
