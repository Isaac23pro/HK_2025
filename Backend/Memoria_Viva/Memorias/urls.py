from django.urls import path
from .views import (
    MemoriaListCreateView, MemoriaRetrieveUpdateDestroyView,
    MedioListCreateView, MedioRetrieveUpdateDestroyView,
    ComentarioMemoriaListCreateView, ComentarioMemoriaRetrieveUpdateDestroyView,
    ReaccionMemoriaListCreateView, ReaccionMemoriaRetrieveUpdateDestroyView
)

urlpatterns = [
    # Endpoints para Memorias
    path('memorias/', MemoriaListCreateView.as_view(), name='memoria-list-create'),
    path('memorias/<int:pk>/', MemoriaRetrieveUpdateDestroyView.as_view(), name='memoria-detail'),
    # Endpoints para Medios
    path('medios/', MedioListCreateView.as_view(), name='medio-list-create'),
    path('medios/<int:pk>/', MedioRetrieveUpdateDestroyView.as_view(), name='medio-detail'),
    # Endpoints para Comentarios de Memoria
    path('comentarios/', ComentarioMemoriaListCreateView.as_view(), name='comentario-list-create'),
    path('comentarios/<int:pk>/', ComentarioMemoriaRetrieveUpdateDestroyView.as_view(), name='comentario-detail'),
    # Endpoints para Reacciones de Memoria
    path('reacciones/', ReaccionMemoriaListCreateView.as_view(), name='reaccion-list-create'),
    path('reacciones/<int:pk>/', ReaccionMemoriaRetrieveUpdateDestroyView.as_view(), name='reaccion-detail'),
]
