from django.urls import path
from .views import UsuarioListCreateView, UsuarioRetrieveUpdateDestroyView, LoginView, LogoutView

urlpatterns = [
    path('', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
    path('login/', LoginView.as_view(), name='usuario-login'),
    path('logout/', LogoutView.as_view(), name='usuario-logout'),
]
