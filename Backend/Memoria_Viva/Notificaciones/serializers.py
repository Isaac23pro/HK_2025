from rest_framework import serializers
from .models import Notificacion
from Usuarios.models import Usuario

# Serializador para Notificacion
class NotificacionSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())

    class Meta:
        model = Notificacion
        fields = '__all__'

    def validate_mensaje(self, value):
        if not value or len(value) < 5:
            raise serializers.ValidationError("El mensaje debe tener al menos 5 caracteres.")
        return value
