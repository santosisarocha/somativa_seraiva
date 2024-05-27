from rest_framework import serializers
from .models import UsuarioCustomizado, Categoria, Livro, Emprestimo, EmprestimoLivro

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id', 'email', 'telefone', 'cpf', 'endereco', 'is_active', 'groups', 'user_permissions']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    categoriaFK = CategoriaSerializer(read_only=True)  
    usuarioFK = UsuarioCustomizadoSerializer(read_only=True)  

    class Meta:
        model = Livro
        fields = '__all__'

    # def to_representation(self, instance):
    #     if instance:
    #         representation = super().to_representation(instance)
    #         if instance.status == "APROVADO":
    #             return representation
    #     else: return None


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

class EmprestimoLivroSerializer(serializers.ModelSerializer):
    livroFK = LivroSerializer

    class Meta:
        many = True
        model = EmprestimoLivro
        fields = '__all__'