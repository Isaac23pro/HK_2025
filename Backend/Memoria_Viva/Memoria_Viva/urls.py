"""
URL configuration for Memoria_Viva project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include, re_path
# Importaciones para JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# Importaciones para Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Memoria Viva Nicaragua API",
        default_version='v1',
        description="""
        API para la aplicación educativa Memoria Viva Nicaragua.

        **Permisos:**
        - La mayoría de los endpoints requieren autenticación JWT (Bearer Token).
        - Solo usuarios autenticados pueden crear, editar o borrar recursos.
        - La lectura (GET) es pública para la mayoría de los recursos.
        - Permisos avanzados por rol (Administrador, Moderador, Usuario) están preparados para futuras versiones.

        **Autenticación:**
        - Obtén tu token en `/api/token/` usando nombre_usuario y contraseña.
        - Usa el token en el header: `Authorization: Bearer <tu_token>`
        
        **Swagger:**
        - Puedes probar los endpoints protegidos usando el botón "Authorize" arriba e ingresando tu token JWT.
        """,
        contact=openapi.Contact(email="soporte@memoriaviva.ni"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas de las apps (se agregarán más adelante)
    path('usuarios/', include('Usuarios.urls')),
    path('memorias/', include('Memorias.urls')),
    path('saberes/', include('Saberes.urls')),
    path('eventos/', include('Eventos.urls')),
    path('retos/', include('Retos.urls')),
    path('notificaciones/', include('Notificaciones.urls')),
    path('catalogos/', include('Catalogos.urls')),
    # Endpoints de autenticación JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Documentación Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
