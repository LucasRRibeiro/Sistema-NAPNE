from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

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
class LaudoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Laudo
    fields = ['descricao', 'data']
    success_url = reverse_lazy('listar-laudo')
    success_message = "Laudo criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Laudo', 'botao': 'Salvar'}

class NapneCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('listar-napne')
    success_message = "Napne criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Napne', 'botao': 'Salvar'}

class ResponsavelCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'email', 'cpf', 'cidade']
    success_url = reverse_lazy('listar-responsavel')
    success_message = "Responsável criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Responsável', 'botao': 'Salvar'}

class IndicativoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo']
    success_url = reverse_lazy('listar-indicativo')
    success_message = "Indicativo criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Indicativo', 'botao': 'Salvar'}

class AlunoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'endereco', 'fone', 'email', 'curso', 'ano', 'cpf', 'rg', 'cidade', 'data_nasc', 'laudo', 'responsavel']
    success_url = reverse_lazy('listar-aluno')
    success_message = "Aluno criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de alunos', 'botao': 'Salvar'}

class InteracoesCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'aluno']
    success_url = reverse_lazy('listar-interacoes')
    success_message = "Interação criada com sucesso!"
    extra_context = {'titulo': 'Cadastro de Interações', 'botao': 'Salvar'}

class ServidorCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Servidor
    fields = ['siape', 'nome', 'endereco', 'fone', 'email', 'cidade', 'tipo', 'napne']
    success_url = reverse_lazy('listar-servidor')
    success_message = "Servidor criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Servidor', 'botao': 'Salvar'}


# UPDATE
class LaudoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Laudo
    fields = ['descricao', 'data']
    success_url = reverse_lazy('listar-laudo')
    success_message = "Laudo atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Laudo', 'botao': 'Salvar'}

class NapneUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('listar-napne')
    success_message = "Napne atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Napne', 'botao': 'Salvar'}

class ResponsavelUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'email', 'cpf', 'cidade']
    success_url = reverse_lazy('listar-responsavel')
    success_message = "Responsável atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Responsável', 'botao': 'Salvar'}

class IndicativoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo']
    success_url = reverse_lazy('listar-indicativo')
    success_message = "Indicativo atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Indicativo', 'botao': 'Salvar'}

class AlunoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'endereco', 'fone', 'email', 'curso', 'ano', 'cpf', 'rg', 'cidade', 'data_nasc', 'laudo', 'responsavel']
    success_url = reverse_lazy('listar-aluno')
    success_message = "Aluno atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de alunos', 'botao': 'Salvar'}

class InteracoesUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'aluno']
    success_url = reverse_lazy('listar-interacoes')
    success_message = "Interação atualizada com sucesso!"
    extra_context = {'titulo': 'Atualização de Interações', 'botao': 'Salvar'}

class ServidorUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Servidor
    fields = ['siape', 'nome', 'endereco', 'fone', 'email', 'cidade', 'tipo', 'napne']
    success_url = reverse_lazy('listar-servidor')
    success_message = "Servidor atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Servidor', 'botao': 'Salvar'}


# DELETE
class LaudoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Laudo
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-laudo')
    success_message = "Laudo excluído com sucesso!"

class NapneDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Napne
    success_url = reverse_lazy('listar-napne')
    success_message = "Napne excluído com sucesso!"

class ResponsavelDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Responsavel
    success_url = reverse_lazy('listar-responsavel')
    success_message = "Responsável excluído com sucesso!"

class IndicativoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Indicativo
    success_url = reverse_lazy('listar-indicativo')
    success_message = "Indicativo excluído com sucesso!"

class AlunoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Aluno
    success_url = reverse_lazy('listar-aluno')
    success_message = "Aluno excluído com sucesso!"

class InteracoesDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Interacoes
    success_url = reverse_lazy('listar-interacoes')
    success_message = "Interação excluída com sucesso!"

class ServidorDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Servidor
    success_url = reverse_lazy('listar-servidor')
    success_message = "Servidor excluído com sucesso!"


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
