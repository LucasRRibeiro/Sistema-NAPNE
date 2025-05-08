from django.views.generic import TemplateView

# 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Importar as classes criadas em modelos.py 
from.models import Laudo, Napne

# Função que converte o nome de uma URL na rota dela
from django.urls import reverse_lazy

class IndexView (TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

class LaudoCreate(CreateView):
    template_name = 'paginas/form.html' # arquivo html com o <form>
    model = Laudo #classe criada no models
    fields = [ 'descricao', 'data' ] # lista com os nome dos atributos
    success_url = reverse_lazy('index') # name da url para redirecionar
    extra_context = { 'titulo' : 'Cadastro de Laudo' }

class NapneCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = { 'titulo' : 'Cadastro de Napne' }
