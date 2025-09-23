
from django.urls import path
from .views import IndexView, SobreView, MenuView, MenuListasView
from .views import LaudoCreate, NapneCreate, ResponsavelCreate, IndicativoCreate, AlunoCreate, InteracoesCreate, IntervencaoCreate, ServidorCreate, CursoCreate, DisciplinaCreate, ProfessorCreate ,PteCreate, RelatorioPteCreate
from .views import LaudoUpdate, NapneUpdate, ResponsavelUpdate, IndicativoUpdate, AlunoUpdate, InteracoesUpdate, IntervencaoUpdate, ServidorUpdate, CursoUpdate, DisciplinaUpdate, ProfessorUpdate, PteUpdate, RelatorioPteUpdate
from .views import LaudoDelete, NapneDelete, ResponsavelDelete, IndicativoDelete, AlunoDelete, InteracoesDelete, IntervencaoDelete, ServidorDelete, CursoDelete, DisciplinaDelete, ProfessorDelete, PteDelete, RelatorioPteDelete
from .views import LaudoList, NapneList, ResponsavelList, IndicativoList, AlunoList, InteracoesList, IntervencaoList, ServidorList, CursoList, DisciplinaList, ProfessorList, PteList, RelatorioPteList
from django.contrib.auth import views as auth_views
from .views import CadastroUsuarioView
from .views import MeusLaudos, MinhasInteracoes, MeusIndicativos, MeusPtes, MeusRelatoriosPte, MinhasIntervencoes
from .views import NapnePdf, ServidorPdf, ResponsavelPdf, AlunoPdf, LaudoPdf, IndicativoPdf, InteracoesPdf, IntervencaoPdf, CursoPdf, DisciplinaPdf, ProfessorPdf, PtePdf, RelatorioPtePdf

urlpatterns = [

    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),

    #Criar rota para página de login
    path('login/', auth_views.LoginView.as_view(
        template_name = 'paginas/login.html',
         extra_context = {
            'titulo': 'Autenticação',
            'botao': 'Entrar'}   
    ), name="login"),

    path('atualizar/senha/', auth_views.PasswordChangeView.as_view(
    template_name = 'paginas/form.html',
        extra_context = {
        'titulo': 'Atualizar senha',
        'botao': 'Salvar'}   
    ), name="senha"),
    #detail view para os models


    
    #Criar uma rota de logout
    path('sair/', auth_views.LogoutView.as_view(), name="logout"),
    
    path('', IndexView.as_view(), name="index"), # URL para a página
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('menu/', MenuView.as_view(), name="menu"),
    path('menu/listas/', MenuListasView.as_view(), name="menu-listas"),
    
    path('cadastrar/laudo/', LaudoCreate.as_view(), name="cadastrar-laudo"),
    path('cadastrar/napne/', NapneCreate.as_view(), name="cadastrar-napne"),
    path('cadastrar/responsavel/', ResponsavelCreate.as_view(), name="cadastrar-responsavel"),
    path('cadastrar/indicativo/', IndicativoCreate.as_view(), name="cadastrar-indicativo"),
    path('cadastrar/aluno/', AlunoCreate.as_view(), name="cadastrar-aluno"),
    path('cadastrar/interacoes/', InteracoesCreate.as_view(), name="cadastrar-interacoes"),
    path('cadastrar/intervencao/', IntervencaoCreate.as_view(), name="cadastrar-intervencao"),
    path('cadastrar/servidor/', ServidorCreate.as_view(), name="cadastrar-servidor"),
    path('cadastrar/curso/', CursoCreate.as_view(), name="cadastrar-curso"),
    path('cadastrar/disciplina/', DisciplinaCreate.as_view(), name="cadastrar-disciplina"),
    path('cadastrar/professor/', ProfessorCreate.as_view(), name="cadastrar-professor"),
    path('cadastrar/pte/', PteCreate.as_view(), name="cadastrar-pte"),
    path('cadastrar/relatorio-pte/', RelatorioPteCreate.as_view(), name="cadastrar-relatorio-pte"),

    path('editar/laudo/<int:pk>/', LaudoUpdate.as_view(), name="editar-laudo"),
    path('editar/napne/<int:pk>/', NapneUpdate.as_view(), name="editar-napne"),
    path('editar/responsavel/<int:pk>/', ResponsavelUpdate.as_view(), name="editar-responsavel"),
    path('editar/indicativo/<int:pk>/', IndicativoUpdate.as_view(), name="editar-indicativo"),
    path('editar/aluno/<int:pk>/', AlunoUpdate.as_view(), name="editar-aluno"),
    path('editar/interacoes/<int:pk>/', InteracoesUpdate.as_view(), name="editar-interacoes"),
    path('editar/intervencao/<int:pk>/', IntervencaoUpdate.as_view(), name="editar-intervencao"),
    path('editar/servidor/<int:pk>/', ServidorUpdate.as_view(), name="editar-servidor"),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name="editar-curso"),
    path('editar/disciplina/<int:pk>/', DisciplinaUpdate.as_view(), name="editar-disciplina"),
    path('editar/professor/<int:pk>/', ProfessorUpdate.as_view(), name="editar-professor"),
    path('editar/pte/<int:pk>/', PteUpdate.as_view(), name="editar-pte"),
    path('editar/relatorio-pte/<int:pk>/', RelatorioPteUpdate.as_view(), name="editar-relatorio-pte"),

    path('excluir/laudo/<int:pk>/', LaudoDelete.as_view(), name="excluir-laudo"),
    path('excluir/napne/<int:pk>/', NapneDelete.as_view(), name="excluir-napne"),
    path('excluir/responsavel/<int:pk>/', ResponsavelDelete.as_view(), name="excluir-responsavel"),
    path('excluir/indicativo/<int:pk>/', IndicativoDelete.as_view(), name="excluir-indicativo"),
    path('excluir/aluno/<int:pk>/', AlunoDelete.as_view(), name="excluir-aluno"),
    path('excluir/interacoes/<int:pk>/', InteracoesDelete.as_view(), name="excluir-interacoes"),
    path('excluir/intervencao/<int:pk>/', IntervencaoDelete.as_view(), name="excluir-intervencao"),
    path('excluir/servidor/<int:pk>/', ServidorDelete.as_view(), name="excluir-servidor"),
    path('excluir/curso/<int:pk>/', CursoDelete.as_view(), name="excluir-curso"),
    path('excluir/disciplina/<int:pk>/', DisciplinaDelete.as_view(), name="excluir-disciplina"),
    path('excluir/professor/<int:pk>/', ProfessorDelete.as_view(), name="excluir-professor"),
    path('excluir/pte/<int:pk>/', PteDelete.as_view(), name="excluir-pte"),
    path('excluir/relatorio-pte/<int:pk>/', RelatorioPteDelete.as_view(), name="excluir-relatorio-pte"),

    path('listar/laudo/', LaudoList.as_view(), name="listar-laudo"),
    path('listar/napne/', NapneList.as_view(), name="listar-napne"),
    path('listar/responsavel/', ResponsavelList.as_view(), name="listar-responsavel"),
    path('listar/indicativo/', IndicativoList.as_view(), name="listar-indicativo"),
    path('listar/aluno/', AlunoList.as_view(), name="listar-aluno"),
    path('listar/interacoes/', InteracoesList.as_view(), name="listar-interacoes"),
    path('listar/intervencao/', IntervencaoList.as_view(), name="listar-intervencao"),
    path('listar/servidor/', ServidorList.as_view(), name="listar-servidor"),
    path('listar/curso/', CursoList.as_view(), name="listar-curso"),
    path('listar/disciplina/', DisciplinaList.as_view(), name="listar-disciplina"),
    path('listar/professor/', ProfessorList.as_view(), name="listar-professor"),
    path('listar/pte/', PteList.as_view(), name="listar-pte"),
    path('listar/relatorio-pte/', RelatorioPteList.as_view(), name="listar-relatorio-pte"),

    path("listar/meus-laudos/", MeusLaudos.as_view(), name="meus-laudos"),
    path("listar/minhas-interacoes/", MinhasInteracoes.as_view(), name="minhas-interacoes"),
    path("listar/meus-indicativos/", MeusIndicativos.as_view(), name="meus-indicativos"),
    path("listar/meus-pte/", MeusPtes.as_view(), name="meus-pte"),
    path("listar/meus-relatorios-pte/", MeusRelatoriosPte.as_view(), name="meus-relatorios-pte"),
    path("listar/minhas-intervencoes/", MinhasIntervencoes.as_view(), name="minhas-intervencoes"),

    path('pdf/napne/<int:pk>/', NapnePdf, name="pdf-napne"),
    path('pdf/servidor/<int:pk>/', ServidorPdf, name="pdf-servidor"),
    path('pdf/responsavel/<int:pk>/', ResponsavelPdf, name="pdf-responsavel"),
    path('pdf/aluno/<int:pk>/', AlunoPdf, name="pdf-aluno"),
    path('pdf/laudo/<int:pk>/', LaudoPdf, name="pdf-laudo"),
    path('pdf/indicativo/<int:pk>/', IndicativoPdf, name="pdf-indicativo"),
    path('pdf/interacoes/<int:pk>/', InteracoesPdf, name="pdf-interacoes"),
    path('pdf/intervencao/<int:pk>/', IntervencaoPdf, name="pdf-intervencao"),
    path('pdf/curso/<int:pk>/', CursoPdf, name="pdf-curso"),
    path('pdf/disciplina/<int:pk>/', DisciplinaPdf, name="pdf-disciplina"),
    path('pdf/professor/<int:pk>/', ProfessorPdf, name="pdf-professor"),
    path('pdf/pte/<int:pk>/', PtePdf, name="pdf-pte"),
    path('pdf/relatorio-pte/<int:pk>/', RelatorioPtePdf, name="pdf-relatorio-pte"), 
]

