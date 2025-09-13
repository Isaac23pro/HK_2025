from django.urls import path
from .views import NotificacionListCreateView, NotificacionRetrieveUpdateDestroyView

urlpatterns = [
    path('notificaciones/', NotificacionListCreateView.as_view(), name='notificacion-list-create'),
    path('notificaciones/<int:pk>/', NotificacionRetrieveUpdateDestroyView.as_view(), name='notificacion-detail'),
]
