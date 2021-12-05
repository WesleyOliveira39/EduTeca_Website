from django.urls import path
from .views import *

# path('endereco/', MinhaView.as_view(), name='nome-da-url'),
urlpatterns = [
    path('', InicioView.as_view(), name='index'),
    path('inicio', Inicio1View.as_view(), name='index1'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('parceria/', ParceriaView.as_view(), name='parceria'),  
    path('acervo/<int:pk>/', LivroInfoView.as_view(), name='info-livro'), 
    path('filtroLivro/', LivroFiltroView.as_view(), name='filtro-livro'),
    path('desenvolvedor/', DesenvolvedorView.as_view(), name='desenvolvedor'),
    path('satisfacaoUsuario/', SatisfacaoUserView.as_view(), name='satisfacaoUser'),
    path('satisfacaoBiblioteca/', SatisfacaoBibliView.as_view(), name='satisfacaoBibli'),
    path('faleConosco/', FaleConoscoView.as_view(), name='faleConosco'),
]
