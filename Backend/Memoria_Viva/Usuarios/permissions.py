from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Permite acceso solo a usuarios con rol 'Administrador'.
    """
    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        if not user or not user.is_authenticated:
            return False
        return hasattr(user, 'rol') and getattr(user.rol, 'nombre', '').lower() == 'administrador'

class IsModerator(permissions.BasePermission):
    """
    Permite acceso solo a usuarios con rol 'Moderador' o 'Administrador'.
    """
    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        if not user or not user.is_authenticated:
            return False
        if hasattr(user, 'rol'):
            nombre_rol = getattr(user.rol, 'nombre', '').lower()
            return nombre_rol in ['moderador', 'administrador']
        return False

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permite edición solo al dueño del objeto, lectura pública.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(obj, 'usuario') and obj.usuario == request.user
