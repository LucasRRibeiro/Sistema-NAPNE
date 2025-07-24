from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Laudo, Napne, Responsavel, Indicativo, Aluno, Interacoes, Servidor

# VIEWS PÚBLICAS (sem login necessário)
class IndexView(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

# VIEWS PROTEGIDAS
class MenuView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/menu.html'

class MenuListasView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/menu-listas.html'


# CREATE
class LaudoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Laudo
    fields = ['descricao', 'data']
    success_url = reverse_lazy('listar-laudo')
    extra_context = {'titulo': 'Cadastro de Laudo', 'botao': 'Salvar'}

class NapneCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('listar-napne')
    extra_context = {'titulo': 'Cadastro de Napne', 'botao': 'Salvar'}

class ResponsavelCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'email', 'cpf', 'cidade']
    success_url = reverse_lazy('listar-responsavel')
    extra_context = {'titulo': 'Cadastro de Responsável', 'botao': 'Salvar'}

class IndicativoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo']
    success_url = reverse_lazy('listar-indicativo')
    extra_context = {'titulo': 'Cadastro de Indicativo', 'botao': 'Salvar'}

class AlunoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'endereco', 'fone', 'email', 'curso', 'ano', 'cpf', 'rg', 'cidade', 'data_nasc', 'laudo', 'responsavel']
    success_url = reverse_lazy('listar-aluno')
    extra_context = {'titulo': 'Cadastro de alunos', 'botao': 'Salvar'}

class InteracoesCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'aluno']
    success_url = reverse_lazy('listar-interacoes')
    extra_context = {'titulo': 'Cadastro de Interações', 'botao': 'Salvar'}

class ServidorCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Servidor
    fields = ['siape', 'nome', 'endereco', 'fone', 'email', 'cidade', 'tipo', 'napne']
    success_url = reverse_lazy('listar-servidor')
    extra_context = {'titulo': 'Cadastro de Servidor', 'botao': 'Salvar'}


# UPDATE
class LaudoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Laudo
    fields = ['descricao', 'data']
    success_url = reverse_lazy('listar-laudo')
    extra_context = {'titulo': 'Atualização de Laudo', 'botao': 'Salvar'}

class NapneUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('listar-napne')
    extra_context = {'titulo': 'Atualização de Napne', 'botao': 'Salvar'}

class ResponsavelUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'email', 'cpf', 'cidade']
    success_url = reverse_lazy('listar-responsavel')
    extra_context = {'titulo': 'Atualização de Responsável', 'botao': 'Salvar'}

class IndicativoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo']
    success_url = reverse_lazy('listar-indicativo')
    extra_context = {'titulo': 'Atualização de Indicativo', 'botao': 'Salvar'}

class AlunoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'endereco', 'fone', 'email', 'curso', 'ano', 'cpf', 'rg', 'cidade', 'data_nasc', 'laudo', 'responsavel']
    success_url = reverse_lazy('listar-aluno')
    extra_context = {'titulo': 'Atualização de alunos', 'botao': 'Salvar'}

class InteracoesUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'aluno']
    success_url = reverse_lazy('listar-interacoes')
    extra_context = {'titulo': 'Atualização de Interações', 'botao': 'Salvar'}

class ServidorUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Servidor
    fields = ['siape', 'nome', 'endereco', 'fone', 'email', 'cidade', 'tipo', 'napne']
    success_url = reverse_lazy('listar-servidor')
    extra_context = {'titulo': 'Atualização de Servidor', 'botao': 'Salvar'}


# DELETE
class LaudoDelete(LoginRequiredMixin, DeleteView):
    model = Laudo
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-laudo')

class NapneDelete(LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Napne
    success_url = reverse_lazy('listar-napne')

class ResponsavelDelete(LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Responsavel
    success_url = reverse_lazy('listar-responsavel')

class IndicativoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Indicativo
    success_url = reverse_lazy('listar-indicativo')

class AlunoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Aluno
    success_url = reverse_lazy('listar-aluno')

class InteracoesDelete(LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Interacoes
    success_url = reverse_lazy('listar-interacoes')

class ServidorDelete(LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Servidor
    success_url = reverse_lazy('listar-servidor')


# LIST
class LaudoList(LoginRequiredMixin, ListView):
    model = Laudo
    template_name = "paginas/listas/laudo.html"

class NapneList(LoginRequiredMixin, ListView):
    model = Napne
    template_name = "paginas/listas/napne.html"

class ResponsavelList(LoginRequiredMixin, ListView):
    model = Responsavel
    template_name = "paginas/listas/responsavel.html"

class IndicativoList(LoginRequiredMixin, ListView):
    model = Indicativo
    template_name = "paginas/listas/indicativo.html"

class AlunoList(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = "paginas/listas/aluno.html"

class InteracoesList(LoginRequiredMixin, ListView):
    model = Interacoes
    template_name = "paginas/listas/interacoes.html"

class ServidorList(LoginRequiredMixin, ListView):
    model = Servidor
    template_name = "paginas/listas/servidor.html"
