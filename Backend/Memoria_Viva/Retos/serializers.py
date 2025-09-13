from rest_framework import serializers
from .models import Reto, ProgresoReto, ReaccionReto
from Usuarios.models import Usuario

# Serializador para Reto
class RetoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Reto
        fields = '__all__'

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
