
from django.urls import path
from .views import IndexView, SobreView
from .views import LaudoCreate, NapneCreate

from .views import LaudoUptade

urlpatterns = [
    path('', IndexView.as_view(), name="index"), # URL para a página
    path('sobre/', SobreView.as_view(), name="sobre"),

    path('cadastrar/laudo/', LaudoCreate.as_view(), name="cadastrar-laudo"),
    path('cadastrar/napne/', NapneCreate.as_view(), name="cadastrar-napne"),

    path('editar/laudo/<int:pk>/', LaudoUptade.as_view(), name="editar-laudo"),
]

