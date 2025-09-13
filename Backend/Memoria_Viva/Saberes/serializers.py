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
