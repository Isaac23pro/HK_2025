from rest_framework import serializers
from Catalogos.models import Rol, Localizacion
from .models import Usuario

# Serializer para el modelo Rol
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        ref_name = 'UsuariosRol'

# Serializer para el modelo Localizacion
class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacion
        fields = '__all__'
        ref_name = 'UsuariosLocalizacion'

# Serializer para el modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer(read_only=True)
    localizacion = LocalizacionSerializer(read_only=True)
    rol_id = serializers.PrimaryKeyRelatedField(queryset=Rol.objects.all(), source='rol', write_only=True)
    localizacion_id = serializers.PrimaryKeyRelatedField(queryset=Localizacion.objects.all(), source='localizacion', write_only=True, required=False, allow_null=True)

    class Meta:
        model = Usuario
        fields = [
            'id', 'nombre', 'apellido', 'nombre_usuario', 'correo_electronico',
            'contrasena_hash', 'rol', 'rol_id', 'tipo_usuario', 'institucion_educativa',
            'comunidad', 'localizacion', 'localizacion_id', 'fecha_registro', 'activo'
        ]
        extra_kwargs = {
            'contrasena_hash': {'write_only': True}
        }

    def validate_nombre(self, value):
        if not value or len(value) < 2:
            raise serializers.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return value

    def validate_nombre_usuario(self, value):
        if not value or len(value) < 4:
            raise serializers.ValidationError("El nombre de usuario debe tener al menos 4 caracteres.")
        return value

    def validate_correo_electronico(self, value):
        if '@' not in value:
            raise serializers.ValidationError("Debe ser un correo electrónico válido.")
        return value

    def validate_contrasena_hash(self, value):
        if not value or len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return value
