from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Laudo, Napne, Responsavel, Indicativo, Aluno, Interacoes, Servidor, Curso, Disciplina, Professor, Pte, Intervencao, RelatorioPte
from django.shortcuts import get_object_or_404, render

from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm
#Controle de grupo (Importação do Braces)
from braces.views import GroupRequiredMixin

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
class TelaInicioView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/tela-inicio.html'

class MenuView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/menu.html'

class MenuListasView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/menu-listas.html'


# CREATE
class NapneCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenadora"
    template_name = 'paginas/form.html'
    model = Napne
    fields = ['data_criacao', 'descricao']
    success_url = reverse_lazy('listar-napne')
    success_message = "Napne criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Napne', 'botao': 'Salvar'}

#adicione email em servidor após endereco
class ServidorCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenadora"
    template_name = 'paginas/form.html'
    model = Servidor
    fields = ['siape', 'nome', 'endereco', 'email', 'fone', 'cidade', 'tipo', 'napne']
    success_url = reverse_lazy('listar-servidor')
    success_message = "Servidor criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Servidor', 'botao': 'Salvar'}

    def form_valid(self, form):
        # O campo usuario recebe automaticamente quem está logado
        form.instance.usuario = self.request.user
        return super().form_valid(form)

def form_valid(self, form):
    # Cria o objeto servidor, mas ainda não salva no banco
    servidor = form.save(commit=False)

    username = str(servidor.siape)
    password = User.objects.make_random_password()

    # Verifica se já existe um usuário com esse username
    if not User.objects.filter(username=username).exists():
        # Cria o usuário
        usuario = User.objects.create_user(username=username, password=password)
        usuario.save()

        # Associa o usuário ao servidor
        servidor.usuario = usuario

        # Salva o servidor no banco agora que o usuário está definido
        servidor.save()

        # Adiciona o usuário ao grupo "Servidor"
        grupo, criado = Group.objects.get_or_create(name='Servidor')
        usuario.groups.add(grupo)

    else:
        form.add_error('siape', 'Já existe um servidor com esse SIAPE.')
        return self.form_invalid(form)

    return super().form_valid(form)

class ResponsavelCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'email', 'cidade', 'servidor']
    success_url = reverse_lazy('listar-responsavel')
    success_message = "Responsável criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Responsável', 'botao': 'Salvar'}

    def form_valid(self, form):
        # O campo usuario recebe automaticamente quem está logado
        form.instance.usuario = self.request.user
        return super().form_valid(form)

def form_valid(self, form):
    # Usa o email como username
    username = form.instance.email
    password = User.objects.make_random_password()  # gera senha aleatória segura

    # Verifica se já existe um usuário com esse username
    if not User.objects.filter(username=username).exists():
        # Cria o usuário
        usuario = User.objects.create_user(username=username, password=password, email=form.instance.email)
        usuario.save()

        # Busca ou cria o grupo "Responsavel" e adiciona o usuário a esse grupo
        grupo, criado = Group.objects.get_or_create(name='Responsavel')
        usuario.groups.add(grupo)

        # Associa o usuário criado ao responsável do formulário
        form.instance.usuario = usuario
    else:
        # Retorna erro no formulário dizendo que já existe
        form.add_error('email', 'Já existe um responsável com este email.')
        return self.form_invalid(form)

    return super().form_valid(form)

class CursoCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Curso
    fields = ['nome', 'serie']
    success_url = reverse_lazy('listar-curso')
    success_message = "Curso criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Curso', 'botao': 'Salvar'}

class DisciplinaCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Disciplina
    fields = ['nome', 'curso']
    success_url = reverse_lazy('listar-disciplina')
    success_message = "Disciplina criada com sucesso!"
    extra_context = {'titulo': 'Cadastro de Disciplina', 'botao': 'Salvar'}

class ProfessorCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Professor
    fields = ['nome', 'disciplina']
    success_url = reverse_lazy('listar-professor')
    success_message = "Professor criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Professor', 'botao': 'Salvar'}

class AlunoCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'cpf', 'cidade', 'endereco', 'fone', 'email', 'data_nasc', 'rg', 'responsavel', 'curso']
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

class LaudoCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = u"Coordenadora"
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
    

class InteracoesCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'aluno', 'professor']
    success_url = reverse_lazy('listar-interacoes')
    success_message = "Interação criada com sucesso!"
    extra_context = {'titulo': 'Cadastro de Interações', 'botao': 'Salvar'}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        # Aqui você pode adicionar lógica adicional se necessário
        return super().form_valid(form)

class IndicativoCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo', 'aluno', 'professor']
    success_url = reverse_lazy('listar-indicativo')
    success_message = "Indicativo criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Indicativo', 'botao': 'Salvar'}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        # Aqui você pode adicionar lógica adicional se necessário
        return super().form_valid(form)

class IntervencaoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Intervencao
    fields = ['data', 'descricao', 'aluno', 'professor']
    success_url = reverse_lazy('listar-intervencao')
    success_message = "Intervenção criada com sucesso!"
    extra_context = {'titulo': 'Cadastro de Intervenção', 'botao': 'Salvar'}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        # Aqui você pode adicionar lógica adicional se necessário
        return super().form_valid(form)

class PteCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = u"Coordenadora"
    template_name = 'paginas/form.html'
    model = Pte
    fields = ['data_criacao', 'aluno', 'ano_letivo', 'componente_curricular', 'professor_responsavel', 'periodo_inicio', 'periodo_fim', 'potencialidades_dificuldades_habilidades', 'recursos_servicos_procedimentos', 'expectativas_aprendizagem', 'conteudos_previstos', 'instrumentos_avaliativos', 'anexos', 'informacoes_adicionais']
    success_url = reverse_lazy('listar-pte')
    success_message = "PTE criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de PTE', 'botao': 'Salvar'}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        # Aqui você pode adicionar lógica adicional se necessário
        return super().form_valid(form)

class RelatorioPteCreate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    group_required = u"Coordenadora"
    template_name = 'paginas/form.html'
    model = RelatorioPte
    fields = ['pte', 'data', 'rel_expectativas_nao_alcancadas', 'rel_conteudos_nao_alcancados', 'rel_avaliacao_recursos_adaptados', 'rel_aspectos_desempenho', 'rel_dificuldades_professor', 'rel_anexos', 'rel_informacoes_adicionais']
    success_url = reverse_lazy('listar-relatorio-pte')
    success_message = "Relatório PTE criado com sucesso!"
    extra_context = {'titulo': 'Cadastro de Relatório PTE', 'botao': 'Salvar'}

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

class ServidorUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Coordenadora"
    template_name = 'paginas/form.html'
    model = Servidor
    fields = ['siape', 'nome', 'endereco', 'email', 'fone', 'cidade', 'tipo', 'napne']
    success_url = reverse_lazy('listar-servidor')
    success_message = "Servidor atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Servidor', 'botao': 'Salvar'}

class ResponsavelUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Responsavel
    fields = ['nome', 'endereco', 'fone', 'email', 'cidade', 'servidor']
    success_url = reverse_lazy('listar-responsavel')
    success_message = "Responsável atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Responsável', 'botao': 'Salvar'}

class CursoUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Curso
    fields = ['nome', 'serie']
    success_url = reverse_lazy('listar-curso')
    success_message = "Curso atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Curso', 'botao': 'Salvar'}

class DisciplinaUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Disciplina
    fields = ['nome', 'curso']
    success_url = reverse_lazy('listar-disciplina')
    success_message = "Disciplina atualizada com sucesso!"
    extra_context = {'titulo': 'Atualização de Disciplina', 'botao': 'Salvar'}

class ProfessorUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Professor
    fields = ['nome', 'disciplina']
    success_url = reverse_lazy('listar-professor')
    success_message = "Professor atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Professor', 'botao': 'Salvar'}

class AlunoUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Aluno
    fields = ['ra', 'nome', 'cpf', 'cidade', 'endereco', 'fone', 'email', 'data_nasc', 'rg', 'responsavel', 'curso']
    success_url = reverse_lazy('listar-aluno')
    success_message = "Aluno atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de alunos', 'botao': 'Salvar'}

class LaudoUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Coordenadora"
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

class InteracoesUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Interacoes
    fields = ['data', 'descricao', 'aluno']
    success_url = reverse_lazy('listar-interacoes')
    success_message = "Interação atualizada com sucesso!"
    extra_context = {'titulo': 'Atualização de Interações', 'botao': 'Salvar'}

        #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Interacoes, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj

class IndicativoUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Indicativo
    fields = ['descricao', 'data', 'indicativo', 'aluno']
    success_url = reverse_lazy('listar-indicativo')
    success_message = "Indicativo atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Indicativo', 'botao': 'Salvar'}

    #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Indicativo, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj
class IntervencaoUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form.html'
    model = Intervencao
    fields = ['data', 'descricao', 'aluno']
    success_url = reverse_lazy('listar-intervencao')
    success_message = "Intervenção atualizada com sucesso!"
    extra_context = {'titulo': 'Atualização de Intervenção', 'botao': 'Salvar'}

    #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Intervencao, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj
class PteUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Coordenadora"
    template_name = 'paginas/form.html'
    model = Pte
    fields = ['data_criacao', 'aluno', 'ano_letivo', 'componente_curricular', 'professor_responsavel', 'periodo_inicio', 'periodo_fim', 'potencialidades_dificuldades_habilidades', 'recursos_servicos_procedimentos', 'expectativas_aprendizagem', 'conteudos_previstos', 'instrumentos_avaliativos', 'anexos', 'informacoes_adicionais']
    success_url = reverse_lazy('listar-pte')
    success_message = "PTE atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de PTE', 'botao': 'Salvar'}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        # Aqui você pode adicionar lógica adicional se necessário
        return super().form_valid(form)
    
    #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Pte, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj

class RelatorioPteUpdate(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Coordenadora"
    template_name = 'paginas/form.html'
    model = RelatorioPte
    fields = ['pte', 'data', 'rel_expectativas_nao_alcancadas', 'rel_conteudos_nao_alcancados', 'rel_avaliacao_recursos_adaptados', 'rel_aspectos_desempenho', 'rel_dificuldades_professor', 'rel_anexos', 'rel_informacoes_adicionais']
    success_url = reverse_lazy('listar-relatorio-pte')
    success_message = "Relatório PTE atualizado com sucesso!"
    extra_context = {'titulo': 'Atualização de Relatório PTE', 'botao': 'Salvar'}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        # Aqui você pode adicionar lógica adicional se necessário
        return super().form_valid(form)
    
    #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(RelatorioPte, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj
    
# DELETE
class NapneDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form-excluir.html'
    model = Napne
    success_url = reverse_lazy('listar-napne')
    success_message = "Napne excluído com sucesso!"

class ServidorDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Coordenadora"
    template_name = 'paginas/form-excluir.html'
    model = Servidor
    success_url = reverse_lazy('listar-servidor')
    success_message = "Servidor excluído com sucesso!"


class ResponsavelDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form-excluir.html'
    model = Responsavel
    success_url = reverse_lazy('listar-responsavel')
    success_message = "Responsável excluído com sucesso!"

class CursoDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form-excluir.html'
    model = Curso
    success_url = reverse_lazy('listar-curso')
    success_message = "Curso excluído com sucesso!"

class DisciplinaDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form-excluir.html'
    model = Disciplina
    success_url = reverse_lazy('listar-disciplina')
    success_message = "Disciplina excluída com sucesso!"

class ProfessorDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form-excluir.html'
    model = Professor
    success_url = reverse_lazy('listar-professor')
    success_message = "Professor excluído com sucesso!"

class AlunoDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form-excluir.html'
    model = Aluno
    success_url = reverse_lazy('listar-aluno')
    success_message = "Aluno excluído com sucesso!"

class LaudoDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Coordenadora"
    model = Laudo
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-laudo')
    success_message = "Laudo excluído com sucesso!"

    #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Laudo, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj

class InteracoesDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form-excluir.html'
    model = Interacoes
    success_url = reverse_lazy('listar-interacoes')
    success_message = "Interação excluída com sucesso!"

 #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Intervencao, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj

class IndicativoDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form-excluir.html'
    model = Indicativo
    success_url = reverse_lazy('listar-indicativo')
    success_message = "Indicativo excluído com sucesso!"

 #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Indicativo, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj

class IntervencaoDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Coordenadora", u"Servidor"]
    template_name = 'paginas/form-excluir.html'
    model = Intervencao
    success_url = reverse_lazy('listar-intervencao')
    success_message = "Intervenção excluída com sucesso!"

 #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Intervencao, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj

class PteDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Coordenadora"
    template_name = 'paginas/form-excluir.html'
    model = Pte
    success_url = reverse_lazy('listar-pte')
    success_message = "PTE excluído com sucesso!"

 #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Pte, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj

class RelatorioPteDelete(GroupRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Coordenadora"
    template_name = 'paginas/form-excluir.html'
    model = RelatorioPte
    success_url = reverse_lazy('listar-relatorio-pte')
    success_message = "Relatório PTE excluído com sucesso!"
 
 #Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(RelatorioPte, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj
    
# LIST
class NapneList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenadora"
    model = Napne
    template_name = "paginas/listas/napne.html"
    
    def get_queryset(self):
        queryset = Napne.objects.all()
        
        # Filtros de pesquisa
        descricao = self.request.GET.get('descricao')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')
        
        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)
        if data_inicio:
            queryset = queryset.filter(data_criacao__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(data_criacao__lte=data_fim)
            
        return queryset.order_by('-data_criacao')

class ServidorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenadora"
    model = Servidor
    template_name = "paginas/listas/servidor.html"

    def get_queryset(self):
        queryset = Servidor.objects.all()
        
        # Filtros de pesquisa
        nome = self.request.GET.get('nome')
        siape = self.request.GET.get('siape')
        email = self.request.GET.get('email')
        tipo = self.request.GET.get('tipo')
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if siape:
            queryset = queryset.filter(siape__icontains=siape)
        if email:
            queryset = queryset.filter(email__icontains=email)
        if tipo:
            queryset = queryset.filter(tipo=tipo)
            
        return queryset.order_by('nome')  

class ResponsavelList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Coordenadora", u"Servidor"]
    model = Responsavel
    template_name = "paginas/listas/responsavel.html"
    
    def get_queryset(self):
        queryset = Responsavel.objects.all()
        
        # Filtros de pesquisa
        nome = self.request.GET.get('nome')
        email = self.request.GET.get('email')
        cidade = self.request.GET.get('cidade')
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if email:
            queryset = queryset.filter(email__icontains=email)
        if cidade:
            queryset = queryset.filter(cidade__icontains=cidade)
            
        return queryset.order_by('nome')

class CursoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Coordenadora", u"Servidor"]
    model = Curso
    template_name = "paginas/listas/curso.html"
    
    def get_queryset(self):
        queryset = Curso.objects.all()
        
        # Filtros de pesquisa
        nome = self.request.GET.get('nome')
        serie = self.request.GET.get('serie')
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if serie:
            queryset = queryset.filter(serie=serie)
            
        return queryset.order_by('nome')

class DisciplinaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Coordenadora", u"Servidor"]
    model = Disciplina
    template_name = "paginas/listas/disciplina.html"
    
    def get_queryset(self):
        queryset = Disciplina.objects.all()
        
        # Filtros de pesquisa
        nome = self.request.GET.get('nome')
        curso = self.request.GET.get('curso')
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if curso:
            queryset = queryset.filter(curso_id=curso)
            
        return queryset.order_by('nome')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all().order_by('nome')
        return context

class ProfessorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Coordenadora", u"Servidor"]
    model = Professor
    template_name = "paginas/listas/professor.html"

class AlunoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Coordenadora", u"Servidor", u"Aluno", u"Responsavel"]
    model = Aluno
    template_name = "paginas/listas/aluno.html"
    
    def get_queryset(self):
        queryset = Aluno.objects.all()
        
        # Filtros de pesquisa
        nome = self.request.GET.get('nome')
        ra = self.request.GET.get('ra')
        cidade = self.request.GET.get('cidade')
        curso = self.request.GET.get('curso')
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if ra:
            queryset = queryset.filter(ra__icontains=ra)
        if cidade:
            queryset = queryset.filter(cidade__icontains=cidade)
        if curso:
            queryset = queryset.filter(curso_id=curso)
            
        return queryset.order_by('nome')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all().order_by('nome')
        return context

class LaudoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenadora"
    model = Laudo
    template_name = "paginas/listas/laudo.html"
    
    def get_queryset(self):
        queryset = Laudo.objects.all()
        
        # Filtros de pesquisa
        descricao = self.request.GET.get('descricao')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')
        
        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)
        if data_inicio:
            queryset = queryset.filter(data__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(data__lte=data_fim)
            
        return queryset.order_by('-data')

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

class InteracoesList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Coordenadora", u"Servidor"]
    model = Interacoes
    template_name = "paginas/listas/interacoes.html"

class MinhasInteracoes(InteracoesList):
    def get_queryset(self):
       #Como fazer consultas/filtros no django
       #Classe.object.all() - traz todos os objetos
       #Classe.object.filter(atributo=valor, a2-v2) - filtra os objetos pelo campo e valor

       qs = Interacoes.objects.filter(cadastrado_por=self.request.user)
       return qs

class IndicativoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Coordenadora", u"Servidor"]
    model = Indicativo
    template_name = "paginas/listas/indicativo.html"

class MeusIndicativos(IndicativoList):
    def get_queryset(self):
       #Como fazer consultas/filtros no django
       #Classe.object.all() - traz todos os objetos
       #Classe.object.filter(atributo=valor, a2-v2) - filtra os objetos pelo campo e valor

       qs = Indicativo.objects.filter(cadastrado_por=self.request.user)
       return qs

class IntervencaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Coordenadora", u"Servidor"]
    model = Intervencao
    template_name = "paginas/listas/intervencao.html"

class MinhasIntervencoes(IntervencaoList):
    def get_queryset(self):
       #Como fazer consultas/filtros no django
       #Classe.object.all() - traz todos os objetos
       #Classe.object.filter(atributo=valor, a2-v2) - filtra os objetos pelo campo e valor

       qs = Intervencao.objects.filter(cadastrado_por=self.request.user)
       return qs

class PteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenadora"
    model = Pte
    template_name = "paginas/listas/pte.html"

class MeusPtes(PteList):
    def get_queryset(self):
       #Como fazer consultas/filtros no django
       #Classe.object.all() - traz todos os objetos
       #Classe.object.filter(atributo=valor, a2-v2) - filtra os objetos pelo campo e valor

       qs = Pte.objects.filter(cadastrado_por=self.request.user)
       return qs

class RelatorioPteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Coordenadora"
    model = RelatorioPte
    template_name = "paginas/listas/relatorio-pte.html"

class MeusRelatoriosPte(RelatorioPteList):
    def get_queryset(self):
       #Como fazer consultas/filtros no django
       #Classe.object.all() - traz todos os objetos
       #Classe.object.filter(atributo=valor, a2-v2) - filtra os objetos pelo campo e valor

       qs = RelatorioPte.objects.filter(cadastrado_por=self.request.user)
       return qs

def NapnePdf(request, pk):
    napne = get_object_or_404(Napne, pk=pk)
    return render(request, "paginas/pdf/napne.html", {"napne": napne})

def ServidorPdf(request, pk):
    servidor = get_object_or_404(Servidor, pk=pk)
    return render(request, "paginas/pdf/servidor.html", {"servidor": servidor})

def ResponsavelPdf(request, pk):
    responsavel = get_object_or_404(Responsavel, pk=pk)
    return render(request, "paginas/pdf/responsavel.html", {"responsavel": responsavel})

def CursoPdf(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, "paginas/pdf/curso.html", {"curso": curso})

def DisciplinaPdf(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    return render(request, "paginas/pdf/disciplina.html", {"disciplina": disciplina})

def ProfessorPdf(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, "paginas/pdf/professor.html", {"professor": professor})

def AlunoPdf(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, "paginas/pdf/aluno.html", {"aluno": aluno})

def LaudoPdf(request, pk):
    laudo = get_object_or_404(Laudo, pk=pk)
    return render(request, "paginas/pdf/laudo.html", {"laudo": laudo})

def InteracoesPdf(request, pk):
    interacoes = get_object_or_404(Interacoes, pk=pk)
    return render(request, "paginas/pdf/interacoes.html", {"interacoes": interacoes})

def IndicativoPdf(request, pk):
    indicativo = get_object_or_404(Indicativo, pk=pk)
    return render(request, "paginas/pdf/indicativo.html", {"indicativo": indicativo})

def IntervencaoPdf(request, pk):
    intervencao = get_object_or_404(Intervencao, pk=pk)
    return render(request, "paginas/pdf/intervencao.html", {"intervencao": intervencao})

def PtePdf(request, pk):
    pte = get_object_or_404(Pte, pk=pk)
    return render(request, "paginas/pdf/pte.html", {"pte": pte})

def RelatorioPtePdf(request, pk):
    relatoriopte = get_object_or_404(RelatorioPte, pk=pk)
    return render(request, "paginas/pdf/relatorio-pte.html", {"relatoriopte": relatoriopte})

# FIM DAS VIEWS
