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
from .permissions import IsAdmin, IsModerator, IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer


# Vista para listar y crear usuarios
# NOTA: Para lógica avanzada de permisos por rol, usar IsAdmin, IsModerator, IsOwnerOrReadOnly
class UsuarioListCreateView(generics.ListCreateAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer
    
	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
    
	def create(self, request, *args, **kwargs):
		"""
		Crea un nuevo usuario. El password debe venir hasheado desde el frontend por seguridad.
		"""
		return super().create(request, *args, **kwargs)

# Vista para obtener, actualizar o eliminar un usuario específico
# NOTA: Para lógica avanzada de permisos por rol, usar IsAdmin, IsModerator, IsOwnerOrReadOnly
class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
