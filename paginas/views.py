from django.shortcuts import render
from django.views.generic import TemplateView
from cadastros.models import *
from django.views.generic.list import ListView
from django.db.models import Q

# Create your views here.

#class ModeloView(TemplateView): #Herança - Extends em Java
#    template_name = "paginas/modelo.html"
    
class InicioView(ListView):
    model = Acervo
    template_name = "paginas/index.html"
    paginate_by = 10
      
    def get_queryset(self):
        s = self.request.GET.get('seach')
        if s:
            multiple_q = Q(Q(livro__titulo__icontains=s) |
                           Q(livro__autor__nome__icontains=s) | Q(livro__editora__icontains=s) | Q(livro__categoria__descricao__icontains=s))
            acervos = Acervo.objects.filter(multiple_q)
        else:
            acervos = Acervo.objects.all()
        return acervos
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livro_list'] = Acervo.objects.all().order_by("-id")#Ordenar com base no último cadastro
        return context
    
class LivroInfoView (TemplateView):
    template_name = "paginas/info-livro.html"  

    def get_context_data(self, **kwargs):
        context = super(LivroInfoView, self).get_context_data(**kwargs)
        acervos = Acervo.objects.get(pk=self.kwargs.get('pk'))
        acervos.livro.consulta += 1
        acervos.livro.save()
        context['acervo'] = acervos
        return context

class LivroFiltroView (ListView):
    template_name = "paginas/filtro-livro.html"
   
class PesquisarView (TemplateView):
    template_name = "pesquisar/pesquisar.html"     
    
class Inicio1View(TemplateView):
    template_name = "paginas/index1.html"
    
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
    
class ParceriaView(TemplateView):
    template_name = "paginas/parceria.html"
    
class DesenvolvedorView(TemplateView):
    template_name = "paginas/desenvolvedor.html"
    
class SatisfacaoUserView(TemplateView):
    template_name = "paginas/satisfacaoUser.html"
    
class SatisfacaoBibliView(TemplateView):
    template_name = "paginas/satisfacaoBibli.html"    
    
class FaleConoscoView(TemplateView):
    template_name = "paginas/faleConosco.html"
    
    