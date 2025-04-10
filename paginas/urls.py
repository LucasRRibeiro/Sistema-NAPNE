
from django.urls import path
from .views import IndexView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name="index"), # URL para a página
    path('sobre/', SobreView.as_view(), name="sobre"),
]

