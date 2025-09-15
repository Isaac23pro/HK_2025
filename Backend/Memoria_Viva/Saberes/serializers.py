from rest_framework import serializers
from .models import SaberPopular, ComentarioSaber, ReaccionSaber
from Catalogos.models import Categoria, Localizacion
from Usuarios.models import Usuario

# Serializador para SaberPopular
class SaberPopularSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), allow_null=True, required=False)
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    localizacion = serializers.PrimaryKeyRelatedField(queryset=Localizacion.objects.all(), allow_null=True, required=False)
    aprobado_por = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), allow_null=True, required=False)

    class Meta:
        model = SaberPopular
        fields = '__all__'

    def validate_titulo(self, value):
        if not value or len(value) < 5:
            raise serializers.ValidationError("El título debe tener al menos 5 caracteres.")
        return value

    def validate(self, data):
        if data.get('estado') == 'Aprobado' and not data.get('aprobado_por'):
            raise serializers.ValidationError("Debe indicar quién aprueba el saber.")
        return data

# Serializador para ComentarioSaber
class ComentarioSaberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioSaber
        fields = '__all__'

# Serializador para ReaccionSaber
class ReaccionSaberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaccionSaber
        fields = '__all__'
