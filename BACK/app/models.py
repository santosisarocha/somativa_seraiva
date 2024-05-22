from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from .gerenciador import Gerenciador

class UsuarioCustomizado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("endereço de email", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20)
    nome = models.CharField(max_length=150)
    foto = models.CharField(max_length=1000, null=False)
    biografia = models.CharField(max_length=200, null=False)

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    objects = Gerenciador()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

FORMATO = [
    ("E", "EBOOK"),
    ("F", "FISICO"),
]

STATUS = [
    ("P", "PENDENTE"),
    ("A", "APROVADO"),
    ("C", "CANCELADO"),
]

class Livro(models.Model):
    categoriaFK = models.ForeignKey(Categoria, related_name='livroCategoria', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    foto = models.CharField(max_length=1000)
    estrelas = models.IntegerField()
    descricao = models.CharField(max_length=200)
    num_pag = models.IntegerField()
    formato = models.CharField(max_length=20, choices=FORMATO)
    num_edicao = models.IntegerField()
    usuarioFK = models.ForeignKey(UsuarioCustomizado, related_name='livroAutor', on_delete=models.CASCADE)
    ano = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    usuarioFK = models.ForeignKey(UsuarioCustomizado, related_name='emprestimos', on_delete=models.CASCADE)
    dataHora = models.DateField(auto_now_add=True)
    dataDevolucao = models.DateField()
    dataDevolvido = models.DateField(null=True, blank=True)
    precoTotal = models.DecimalField(max_digits=5, decimal_places=2)
    livro = models.ManyToManyField(Livro)

    def __str__(self):
        return self.usuarioFK.nome