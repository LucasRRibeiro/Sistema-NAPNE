from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Laudo, Napne, Responsavel, Indicativo, Aluno, Interacoes, Servidor
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm

# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    model = User
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'titulo': 'Cadastro de Usuário',
        'botao': 'Registrar',
    }

    def form_valid(self, form):
        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        # Busca ou cria um grupo com esse nome
        grupo, criado = Group.objects.get_or_create(name='Estudante')
        # Acessa o objeto criado e adiciona o usuário no grupo acima
        self.object.groups.add(grupo)
        # Retorna a URL de sucesso
        return url


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
class NapneCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('listar-napne')
    success_message = "Napne criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Napne', 'botao': 'Salvar'}

class ServidorCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Servidor
    fields = ['siape', 'nome', 'endereco', 'fone', 'cidade', 'tipo', 'napne']
    success_url = reverse_lazy('listar-servidor')
    success_message = "Servidor criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Servidor', 'botao': 'Salvar'}

    def form_valid(self, form):
        # o username do servidor é o nº do siape sem máscara
        form.instance.siape
        form.instance.siape
        # Verifica se já existe um usuário com esse username
        if not User.objects.filter(username=username).exists():
            # Se não existir, cria o usuário
            usuario = User.objects.create_user(username=username, password=password)
            usuario.save()
            # Busca ou cria o grupo "Servidor" e adiciona o usuário a esse grupo
            grupo, criado = Group.objects.get_or_create(name='Servidor')
            usuario.groups.add(grupo)
            # Associa o usuário criado ao servidor do formulário
            form.instance.usuario = usuario
        else:
            # Retorna erro no formulário dizendo que o siape já está em uso
            form.add_error('siape', 'Já existe um servidor com esse SIAPE.')
            return self.form_invalid(form)

        return super().form_valid(form)

class ResponsavelCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'cpf', 'cidade']
    success_url = reverse_lazy('listar-responsavel')
    success_message = "Responsável criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Responsável', 'botao': 'Salvar'}

    def form_valid(self, form):
        # o username do servidor é o nº do siape sem máscara
        username = form.instance.cpf
        password = form.instance.cpf
        # Verifica se já existe um usuário com esse username
        if not User.objects.filter(username=username).exists():
            # Se não existir, cria o usuário
            usuario = User.objects.create_user(username=username, password=password)
            usuario.save()
            # Busca ou cria o grupo "Servidor" e adiciona o usuário a esse grupo
            grupo, criado = Group.objects.get_or_create(name='Responsavel')
            usuario.groups.add(grupo)
            # Associa o usuário criado ao servidor do formulário
            form.instance.usuario = usuario
        else:
            # Retorna erro no formulário dizendo que o siape já está em uso
            form.add_error('nome', 'Já existe um responsavel com esses dados.')
            return self.form_invalid(form)

        return super().form_valid(form)


class AlunoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'endereco', 'fone', 'curso', 'ano', 'cpf', 'rg', 'cidade', 'data_nasc', 'responsavel']
    success_url = reverse_lazy('listar-aluno')
    success_message = "Aluno criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de alunos', 'botao': 'Salvar'}

    def form_valid(self, form):
        # o username do servidor é o nº do siape sem máscara
        username = form.instance.ra
        password = form.instance.ra
        # Verifica se já existe um usuário com esse username
        if not User.objects.filter(username=username).exists():
            # Se não existir, cria o usuário
            usuario = User.objects.create_user(username=username, password=password)
            usuario.save()
            # Busca ou cria o grupo "Servidor" e adiciona o usuário a esse grupo
            grupo, criado = Group.objects.get_or_create(name='Aluno')
            usuario.groups.add(grupo)
            # Associa o usuário criado ao servidor do formulário
            form.instance.usuario = usuario
        else:
            # Retorna erro no formulário dizendo que o siape já está em uso
            form.add_error('ra', 'Já existe um aluno com esse RA.')
            return self.form_invalid(form)

        return super().form_valid(form)

class LaudoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Laudo
    fields = ['descricao', 'data', 'aluno']
    success_url = reverse_lazy('listar-laudo')
    success_message = "Laudo criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Laudo', 'botao': 'Salvar'}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        # Aqui você pode adicionar lógica adicional se necessário
        return super().form_valid(form)
    

class InteracoesCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'laudo']
    success_url = reverse_lazy('listar-interacoes')
    success_message = "Interação criada com sucesso!"
    extra_context = {'titulo': 'Cadastro de Interações', 'botao': 'Salvar'}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        # Aqui você pode adicionar lógica adicional se necessário
        return super().form_valid(form)

class IndicativoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo', 'laudo']
    success_url = reverse_lazy('listar-indicativo')
    success_message = "Indicativo criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Indicativo', 'botao': 'Salvar'}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        # Aqui você pode adicionar lógica adicional se necessário
        return super().form_valid(form)

# UPDATE
class NapneUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('listar-napne')
    success_message = "Napne atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Napne', 'botao': 'Salvar'}

class ServidorUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Servidor
    fields = ['siape', 'nome', 'endereco', 'fone', 'cidade', 'tipo', 'napne']
    success_url = reverse_lazy('listar-servidor')
    success_message = "Servidor atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Servidor', 'botao': 'Salvar'}

class ResponsavelUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'cpf', 'cidade']
    success_url = reverse_lazy('listar-responsavel')
    success_message = "Responsável atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Responsável', 'botao': 'Salvar'}

class AlunoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'endereco', 'fone', 'curso', 'ano', 'cpf', 'rg', 'cidade', 'data_nasc', 'responsavel']
    success_url = reverse_lazy('listar-aluno')
    success_message = "Aluno atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de alunos', 'botao': 'Salvar'}

class LaudoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Laudo
    # remover o 'cadastrado_por' do fields
    fields = ['descricao', 'data', 'aluno']
    success_url = reverse_lazy('listar-laudo')
    success_message = "Laudo atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Laudo', 'botao': 'Salvar'}

    #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Laudo, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj
     
class InteracoesUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'laudo']
    success_url = reverse_lazy('listar-interacoes')
    success_message = "Interação atualizada com sucesso!"
    extra_context = {'titulo': 'Atualização de Interações', 'botao': 'Salvar'}

class IndicativoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo', 'laudo']
    success_url = reverse_lazy('listar-indicativo')
    success_message = "Indicativo atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Indicativo', 'botao': 'Salvar'}

# DELETE
class NapneDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Napne
    success_url = reverse_lazy('listar-napne')
    success_message = "Napne excluído com sucesso!"

class ServidorDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Servidor
    success_url = reverse_lazy('listar-servidor')
    success_message = "Servidor excluído com sucesso!"


class ResponsavelDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Responsavel
    success_url = reverse_lazy('listar-responsavel')
    success_message = "Responsável excluído com sucesso!"

class AlunoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Aluno
    success_url = reverse_lazy('listar-aluno')
    success_message = "Aluno excluído com sucesso!"

class LaudoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Laudo
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-laudo')
    success_message = "Laudo excluído com sucesso!"

        #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Laudo, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj

class InteracoesDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Interacoes
    success_url = reverse_lazy('listar-interacoes')
    success_message = "Interação excluída com sucesso!"

class IndicativoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Indicativo
    success_url = reverse_lazy('listar-indicativo')
    success_message = "Indicativo excluído com sucesso!"

# LIST
class NapneList(LoginRequiredMixin, ListView):
    model = Napne
    template_name = "paginas/listas/napne.html"

class ServidorList(LoginRequiredMixin, ListView):
    model = Servidor
    template_name = "paginas/listas/servidor.html"  

class ResponsavelList(LoginRequiredMixin, ListView):
    model = Responsavel
    template_name = "paginas/listas/responsavel.html"

class AlunoList(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = "paginas/listas/aluno.html"

class LaudoList(LoginRequiredMixin, ListView):
    model = Laudo
    template_name = "paginas/listas/laudo.html"

class MeusLaudos(LaudoList):
    def get_queryset(self):
       #Como fazer consultas/filtros no django
       #Classe.object.all() - traz todos os objetos
       #Classe.object.filter(atributo=valor, a2-v2) - filtra os objetos pelo campo e valor

       qs = Laudo.objects.filter(cadastrado_por=self.request.user)
       return qs
    
class AlunosLaudos(LaudoList):
    def get_queryset(self):

       qs = Laudo.objects.filter(aluno__usuario=self.request.user)
       return qs

class ResponsavelLaudos(LaudoList):
    def get_queryset(self):

       qs = Laudo.objects.filter(aluno__responsavel__usuario=self.request.user)
       return qs
    
class InteracoesList(LoginRequiredMixin, ListView):
    model = Interacoes
    template_name = "paginas/listas/interacoes.html"

class MinhasInteracoes(InteracoesList):
    def get_queryset(self):
       #Como fazer consultas/filtros no django
       #Classe.object.all() - traz todos os objetos
       #Classe.object.filter(atributo=valor, a2-v2) - filtra os objetos pelo campo e valor

       qs = Interacoes.objects.filter(cadastrado_por=self.request.user)
       return qs
    
class IndicativoList(LoginRequiredMixin, ListView):
    model = Indicativo
    template_name = "paginas/listas/indicativo.html"

class MeusIndicativos(IndicativoList):
    def get_queryset(self):
       #Como fazer consultas/filtros no django
       #Classe.object.all() - traz todos os objetos
       #Classe.object.filter(atributo=valor, a2-v2) - filtra os objetos pelo campo e valor

       qs = Indicativo.objects.filter(cadastrado_por=self.request.user)
       return qs

