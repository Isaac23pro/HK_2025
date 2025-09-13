from django.urls import path
from .views import (
    RolListCreateView, RolRetrieveUpdateDestroyView,
    LocalizacionListCreateView, LocalizacionRetrieveUpdateDestroyView,
    CategoriaListCreateView, CategoriaRetrieveUpdateDestroyView
)

urlpatterns = [
    # Endpoints para Roles
    path('roles/', RolListCreateView.as_view(), name='rol-list-create'),
    path('roles/<int:pk>/', RolRetrieveUpdateDestroyView.as_view(), name='rol-detail'),
    # Endpoints para Localizaciones
    path('localizaciones/', LocalizacionListCreateView.as_view(), name='localizacion-list-create'),
    path('localizaciones/<int:pk>/', LocalizacionRetrieveUpdateDestroyView.as_view(), name='localizacion-detail'),
    # Endpoints para Categorias
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaRetrieveUpdateDestroyView.as_view(), name='categoria-detail'),
]
