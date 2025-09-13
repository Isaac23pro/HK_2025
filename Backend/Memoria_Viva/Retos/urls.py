from django.urls import path
from .views import (
    RetoListCreateView, RetoRetrieveUpdateDestroyView,
    ProgresoRetoListCreateView, ProgresoRetoRetrieveUpdateDestroyView,
    ReaccionRetoListCreateView, ReaccionRetoRetrieveUpdateDestroyView
)

urlpatterns = [
    # Endpoints para Retos
    path('retos/', RetoListCreateView.as_view(), name='reto-list-create'),
    path('retos/<int:pk>/', RetoRetrieveUpdateDestroyView.as_view(), name='reto-detail'),
    # Endpoints para Progreso en Retos
    path('progresos/', ProgresoRetoListCreateView.as_view(), name='progreso-list-create'),
    path('progresos/<int:pk>/', ProgresoRetoRetrieveUpdateDestroyView.as_view(), name='progreso-detail'),
    # Endpoints para Reacciones a Retos
    path('reacciones/', ReaccionRetoListCreateView.as_view(), name='reaccion-reto-list-create'),
    path('reacciones/<int:pk>/', ReaccionRetoRetrieveUpdateDestroyView.as_view(), name='reaccion-reto-detail'),
]
