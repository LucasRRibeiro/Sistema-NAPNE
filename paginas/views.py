from django.urls import reverse_lazy
from django.views.generic import TemplateView

#
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
# Importar as classes criadas em modelos.py
from .models import Laudo, Napne, Responsavel, Indicativo, Aluno, Interacoes, Servidor

# Função que converte o nome de uma URL na rota dela


class IndexView (TemplateView):
    template_name = "paginas/index.html"


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

class MenuView(TemplateView):
    template_name = 'paginas/menu.html'

class MenuListasView(TemplateView):
    template_name = 'paginas/menu-listas.html'


class LaudoCreate(CreateView):
    template_name = 'paginas/form.html'  # arquivo html com o <form>
    model = Laudo  # classe criada no models
    fields = ['descricao', 'data']  # lista com os nome dos atributos
    success_url = reverse_lazy('listar-laudo')  # name da url para redirecionar
    extra_context = {'titulo': 'Cadastro de Laudo',
                       'botao': 'Salvar'}


class NapneCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('listar-napne')
    extra_context = {'titulo': 'Cadastro de Napne',
                       'botao': 'Salvar'}


class ResponsavelCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'email', 'cpf', 'cidade']
    success_url = reverse_lazy('listar-responsavel')
    extra_context = {'titulo': 'Cadastro de Responsável',
                       'botao': 'Salvar'}


class IndicativoCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo']
    success_url = reverse_lazy('listar-indicativo')
    extra_context = {'titulo': 'Cadastro de Indicativo',
                       'botao': 'Salvar'}


class AlunoCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'endereco', 'fone', 'email', 'curso', 'ano',
        'cpf', 'rg',  'cidade', 'data_nasc', 'laudo', 'responsavel']
    success_url = reverse_lazy('listar-aluno')
    extra_context = {'titulo': 'Cadastro de alunos',
                       'botao': 'Salvar'}


class InteracoesCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'aluno']
    success_url = reverse_lazy('listar-interacoes')
    extra_context = {'titulo': 'Cadastro de Interações',
                       'botao': 'Salvar'}


class ServidorCreate(CreateView):
  template_name = 'paginas/form.html'
  model = Servidor
  fields = ['siape', 'nome', 'endereco', 'fone',
      'email', 'cidade', 'tipo', 'napne']
  success_url = reverse_lazy('listar-servidor')
  extra_context = {'titulo': 'Cadastro de Servidor',
                       'botao': 'Salvar'}

    #############################################################################################################


class LaudoUpdate(UpdateView):
 template_name = 'paginas/form.html'  # arquivo html com o <form>
 model = Laudo  # classe criada no models
 fields = ['descricao', 'data']  # lista com os nome dos atributos
 success_url = reverse_lazy('listar-laudo')  # name da url para redirecionar
 extra_context = {'titulo': 'Atualização de Laudo',
                    'botao': 'Salvar'}


class NapneUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('listar-napne')
    extra_context = {'titulo': 'Atualização de Napne',
                     'botao': 'Salvar'}


class ResponsavelUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'email', 'cpf', 'cidade']
    success_url = reverse_lazy('listar-responsavel')
    extra_context = {'titulo': 'Atualização de Responsável',
                     'botao': 'Salvar'}


class IndicativoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo']
    success_url = reverse_lazy('listar-indicativo')
    extra_context = {'titulo': 'Atualização de Indicativo',
                     'botao': 'Salvar'}


class AlunoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'endereco', 'fone', 'email', 'curso', 'ano',
              'cpf', 'rg',  'cidade', 'data_nasc', 'laudo', 'responsavel']
    success_url = reverse_lazy('listar-aluno')
    extra_context = {'titulo': 'Atualização de alunos',
                     'botao': 'Salvar'}


class InteracoesUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'aluno']
    success_url = reverse_lazy('listar-interacoes')
    extra_context = {'titulo': 'Atualização de Interações',
                     'botao': 'Salvar'}


class ServidorUpdate(UpdateView):
  template_name = 'paginas/form.html'
  model = Servidor
  fields = ['siape', 'nome', 'endereco', 'fone',
      'email', 'cidade', 'tipo', 'napne']
  success_url = reverse_lazy('listar-servidor')
  extra_context = {'titulo': 'Atualização de Servidor',
                   'botao': 'Salvar'}

  #############################################################################################################

class LaudoDelete(DeleteView):
   model = Laudo #classe criada no models
   template_name = 'paginas/form-excluir.html' # arquivo html com o <form>
   success_url = reverse_lazy('listar-laudo') # name da url para redirecionar


class NapneDelete(DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Napne
    success_url = reverse_lazy('listar-napne')
   

class ResponsavelDelete(DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Responsavel
    success_url = reverse_lazy('listar-responsavel')
    

class IndicativoDelete(DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Indicativo
    success_url = reverse_lazy('listar-indicativo')
    

class AlunoDelete(DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Aluno
    success_url = reverse_lazy('listar-aluno')
    

class InteracoesDelete(DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Interacoes
    success_url = reverse_lazy('listar-interacoes')
   
class ServidorDelete(DeleteView):
  template_name = 'paginas/form-excluir.html'
  model = Servidor
  success_url = reverse_lazy('listar-servidor')
  
#########################################################################################################################

class LaudoList(ListView):
    model = Laudo
    template_name = "paginas/listas/laudo.html"
    
class NapneList(ListView):
    template_name = "paginas/listas/napne.html"
    model = Napne
   

class ResponsavelList(ListView):
    template_name = "paginas/listas/responsavel.html"
    model = Responsavel
    

class IndicativoList(ListView):
    template_name = "paginas/listas/indicativo.html"
    model = Indicativo
    

class AlunoList(ListView):
    template_name = "paginas/listas/aluno.html"
    model = Aluno
    

class InteracoesList(ListView):
    template_name = "paginas/listas/interacoes.html"
    model = Interacoes
   
class ServidorList(ListView):
  template_name = "paginas/listas/servidor.html"
  model = Servidor
  