from rest_framework import serializers
from .models import Evento
from Catalogos.models import Categoria, Localizacion
from Usuarios.models import Usuario

# Serializador para Evento
class EventoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), allow_null=True, required=False)
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), allow_null=True, required=False)
    localizacion = serializers.PrimaryKeyRelatedField(queryset=Localizacion.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Evento
        fields = '__all__'

    def validate_nombre_evento(self, value):
        if not value or len(value) < 5:
            raise serializers.ValidationError("El nombre del evento debe tener al menos 5 caracteres.")
        return value
