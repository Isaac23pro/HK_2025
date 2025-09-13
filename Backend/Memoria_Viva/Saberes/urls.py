from django.urls import path
from .views import (
    SaberPopularListCreateView, SaberPopularRetrieveUpdateDestroyView,
    ComentarioSaberListCreateView, ComentarioSaberRetrieveUpdateDestroyView,
    ReaccionSaberListCreateView, ReaccionSaberRetrieveUpdateDestroyView
)

urlpatterns = [
    # Endpoints para Saberes Populares
    path('saberes/', SaberPopularListCreateView.as_view(), name='saber-list-create'),
    path('saberes/<int:pk>/', SaberPopularRetrieveUpdateDestroyView.as_view(), name='saber-detail'),
    # Endpoints para Comentarios de Saber
    path('comentarios/', ComentarioSaberListCreateView.as_view(), name='comentario-saber-list-create'),
    path('comentarios/<int:pk>/', ComentarioSaberRetrieveUpdateDestroyView.as_view(), name='comentario-saber-detail'),
    # Endpoints para Reacciones de Saber
    path('reacciones/', ReaccionSaberListCreateView.as_view(), name='reaccion-saber-list-create'),
    path('reacciones/<int:pk>/', ReaccionSaberRetrieveUpdateDestroyView.as_view(), name='reaccion-saber-detail'),
]
