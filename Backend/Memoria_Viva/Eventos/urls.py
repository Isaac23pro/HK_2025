from django.urls import path
from .views import EventoListCreateView, EventoRetrieveUpdateDestroyView

urlpatterns = [
    path('eventos/', EventoListCreateView.as_view(), name='evento-list-create'),
    path('eventos/<int:pk>/', EventoRetrieveUpdateDestroyView.as_view(), name='evento-detail'),
]
