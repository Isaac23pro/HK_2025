from rest_framework import serializers
from .models import Memoria, Medio, ComentarioMemoria, ReaccionMemoria
from Catalogos.models import Categoria, Localizacion
from Usuarios.models import Usuario

# Serializador para Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        ref_name = 'MemoriasCategoria'

# Serializador para Memoria
class MemoriaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source='categoria', write_only=True)
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    localizacion = serializers.PrimaryKeyRelatedField(queryset=Localizacion.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Memoria
        fields = [
            'id', 'titulo', 'descripcion', 'usuario', 'localizacion', 'categoria', 'categoria_id',
            'fecha_creacion', 'estado', 'aprobado_por', 'fecha_aprobacion', 'es_publico', 'activo'
        ]

# Serializador para Medio
class MedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio
        fields = '__all__'

# Serializador para ComentarioMemoria
class ComentarioMemoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioMemoria
        fields = '__all__'

# Serializador para ReaccionMemoria
class ReaccionMemoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaccionMemoria
        fields = '__all__'
