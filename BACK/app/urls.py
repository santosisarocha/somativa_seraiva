from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'usuario', UsuarioCustomizadoView)
router.register(r'categoria',CategoriaView)
router.register(r'livro',LivroView)
router.register(r'emprestimo',EmprestimoView)
router.register(r'emprestimo-livro',EmprestimoLivrosView)

urlpatterns = router.urls