from rest_framework import serializers
from .models import Reto, ProgresoReto, ReaccionReto
from Usuarios.models import Usuario

# Serializador para Reto
class RetoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Reto
        fields = '__all__'

    def validate_titulo(self, value):
        if not value or len(value) < 5:
            raise serializers.ValidationError("El título del reto debe tener al menos 5 caracteres.")
        return value

# Serializador para ProgresoReto
class ProgresoRetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoReto
        fields = '__all__'

# Serializador para ReaccionReto
class ReaccionRetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaccionReto
        fields = '__all__'
