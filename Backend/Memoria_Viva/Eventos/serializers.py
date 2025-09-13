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
