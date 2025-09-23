from django.contrib import admin
from .models import Curso, Laudo, Napne, Responsavel, Indicativo, Aluno, Interacoes, Servidor, Disciplina, Professor, Pte, Intervencao, RelatorioPte

admin.site.register(Laudo)
admin.site.register(Napne)
admin.site.register(Responsavel)
admin.site.register(Indicativo)
admin.site.register(Aluno)
admin.site.register(Interacoes)
admin.site.register(Servidor)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Pte)
admin.site.register(Professor)
admin.site.register(Intervencao)
admin.site.register(RelatorioPte)
# Register your models here.
