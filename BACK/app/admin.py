from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AdminUsuarioCustomizado(UserAdmin):
    model = UsuarioCustomizado
    list_display = ['id', 'email', 'cpf', 'nome']  
    list_display_links = ('id', 'email', 'cpf', 'nome')  
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('nome', 'cpf', 'telefone', 'endereco', 'foto', 'biografia')}), 
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions', 'nome', 'cpf', 'telefone', 'endereco', 'foto', 'biografia',)
        }),
    )
    search_fields = ['email', 'nome']  
    ordering = ['email']

admin.site.register(UsuarioCustomizado, AdminUsuarioCustomizado)



class AdminCategoria(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Categoria,AdminCategoria)

class AdminLivro(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'categoriaFK']
    list_display_links = ('id', 'titulo', 'categoriaFK',)
    search_fields = ('titulo',)
    list_per_page = 10
    
admin.site.register(Livro, AdminLivro)

class AdminEmprestimo(admin.ModelAdmin):
    list_display = ['id', 'usuarioFK', 'dataHora']
    list_display_links = ('id', 'usuarioFK', 'dataHora',)
    search_fields = ('usuarioFK',)
    list_per_page = 10
    
admin.site.register(Emprestimo,AdminEmprestimo)