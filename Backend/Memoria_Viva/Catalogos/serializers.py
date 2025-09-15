from rest_framework import serializers
from .models import Rol, Localizacion, Categoria

# Serializador para Rol
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        ref_name = 'CatalogosRol'

# Serializador para Localizacion
class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacion
        fields = '__all__'
        ref_name = 'CatalogosLocalizacion'

# Serializador para Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        ref_name = 'CatalogosCategoria'
