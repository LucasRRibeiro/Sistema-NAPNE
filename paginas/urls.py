
from django.urls import path
from .views import IndexView, SobreView, MenuView, MenuListasView
from .views import LaudoCreate, NapneCreate, ResponsavelCreate, IndicativoCreate, AlunoCreate, InteracoesCreate, ServidorCreate
from .views import LaudoUpdate, NapneUpdate, ResponsavelUpdate, IndicativoUpdate, AlunoUpdate, InteracoesUpdate, ServidorUpdate
from .views import LaudoDelete, NapneDelete, ResponsavelDelete, IndicativoDelete, AlunoDelete, InteracoesDelete, ServidorDelete
from .views import LaudoList, NapneList, ResponsavelList, IndicativoList, AlunoList, InteracoesList, ServidorList

urlpatterns = [
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
    path('cadastrar/servidor/', ServidorCreate.as_view(), name="cadastrar-servidor"),

    path('editar/laudo/<int:pk>/', LaudoUpdate.as_view(), name="editar-laudo"),
    path('editar/napne/<int:pk>/', NapneUpdate.as_view(), name="editar-napne"),
    path('editar/responsavel/<int:pk>/', ResponsavelUpdate.as_view(), name="editar-responsavel"),
    path('editar/indicativo/<int:pk>/', IndicativoUpdate.as_view(), name="editar-indicativo"),
    path('editar/aluno/<int:pk>/', AlunoUpdate.as_view(), name="editar-aluno"),
    path('editar/interacoes/<int:pk>/', InteracoesUpdate.as_view(), name="editar-interacoes"),
    path('editar/servidor/<int:pk>/', ServidorUpdate.as_view(), name="editar-servidor"),

    path('excluir/laudo/<int:pk>/', LaudoDelete.as_view(), name="excluir-laudo"),
    path('excluir/napne/<int:pk>/', NapneDelete.as_view(), name="excluir-napne"),
    path('excluir/responsavel/<int:pk>/', ResponsavelDelete.as_view(), name="excluir-responsavel"),
    path('excluir/indicativo/<int:pk>/', IndicativoDelete.as_view(), name="excluir-indicativo"),
    path('excluir/aluno/<int:pk>/', AlunoDelete.as_view(), name="excluir-aluno"),
    path('excluir/interacoes/<int:pk>/', InteracoesDelete.as_view(), name="excluir-interacoes"),
    path('excluir/servidor/<int:pk>/', ServidorDelete.as_view(), name="excluir-servidor"),

    path('listar/laudo/', LaudoList.as_view(), name="listar-laudo"),
    path('listar/napne/', NapneList.as_view(), name="listar-napne"),
    path('listar/responsavel/', ResponsavelList.as_view(), name="listar-responsavel"),
    path('listar/indicativo/', IndicativoList.as_view(), name="listar-indicativo"),
    path('listar/aluno/', AlunoList.as_view(), name="listar-aluno"),
    path('listar/interacoes/', InteracoesList.as_view(), name="listar-interacoes"),
    path('listar/servidor/', ServidorList.as_view(), name="listar-servidor")

]

