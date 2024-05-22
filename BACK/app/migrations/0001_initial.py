# Generated by Django 5.0.6 on 2024-05-22 00:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioCustomizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='endereço de email')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=150)),
                ('foto', models.CharField(max_length=1000)),
                ('biografia', models.CharField(max_length=200)),
                ('groups', models.ManyToManyField(related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade', models.IntegerField()),
                ('foto', models.CharField(max_length=1000)),
                ('estrelas', models.IntegerField()),
                ('descricao', models.CharField(max_length=200)),
                ('num_pag', models.IntegerField()),
                ('formato', models.CharField(choices=[('E', 'EBOOK'), ('F', 'FISICO')], max_length=20)),
                ('num_edicao', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('status', models.CharField(choices=[('P', 'PENDENTE'), ('A', 'APROVADO'), ('C', 'CANCELADO')], max_length=20)),
                ('categoriaFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livroCategoria', to='app.categoria')),
                ('usuarioFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livroAutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHora', models.DateField(auto_now_add=True)),
                ('dataDevolucao', models.DateField()),
                ('dataDevolvido', models.DateField(blank=True, null=True)),
                ('precoTotal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('usuarioFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos', to=settings.AUTH_USER_MODEL)),
                ('livro', models.ManyToManyField(to='app.livro')),
            ],
        ),
    ]
