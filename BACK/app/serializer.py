from rest_framework import serializers
from .models import UsuarioCustomizado, Categoria, Livro, Emprestimo

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id', 'email', 'telefone', 'cpf', 'endereco', 'is_active', 'groups', 'user_permissions']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    categoriaFK = CategoriaSerializer(read_only=True)  # Use nested serializer
    usuarioFK = UsuarioCustomizadoSerializer(read_only=True)  # Use nested serializer

    class Meta:
        model = Livro
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    livro = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='titulo'
    )
    usuarioFK = UsuarioCustomizadoSerializer(read_only=True)

    class Meta:
        model = Emprestimo
        fields = '__all__'
