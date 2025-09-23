from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


class Napne(models.Model):
    data_criacao = models.DateField(verbose_name="Data de Criação")
    descricao = models.CharField(max_length=250, verbose_name="Descrição")

    def __str__(self):
        return f"{self.descricao} ({self.data_criacao.strftime('%d/%m/%Y')})"
    
# adicione na classe servidor o email do usuario
class Servidor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='servidor')
    siape = models.PositiveIntegerField(unique=True, verbose_name="SIAPE")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    email = models.EmailField(max_length=254, verbose_name="Email")
    tipo = models.CharField(max_length=50, verbose_name="Tipo")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    fone = models.CharField(max_length=15, verbose_name="Telefone")
    napne = models.ForeignKey(Napne, on_delete=models.CASCADE, verbose_name="NAPNE")

    def __str__(self):
        return f"{self.nome} (SIAPE: {self.siape})"

class Responsavel(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='responsavel')
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    fone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(max_length=254, verbose_name="Email")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    servidor = models.ForeignKey(Servidor, on_delete=models.SET_NULL, verbose_name="Servidor", null=True, blank=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    serie = models.CharField(max_length=50, verbose_name="Série", null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.serie})"


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, verbose_name="Curso", null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.curso.nome})"


class Professor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, verbose_name="Disciplina", null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.disciplina.nome})"

class Aluno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')
    ra = models.CharField(max_length=20, verbose_name="Ra")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    fone = models.CharField(max_length=16, verbose_name="Telefone")
    email = models.EmailField(max_length=254, verbose_name="Email")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    rg = models.CharField(max_length=20, verbose_name="RG")
    responsavel = models.ForeignKey(Responsavel, on_delete=models.SET_NULL, verbose_name="Responsável", null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")

    def __str__(self):
        return f"{self.nome} (RA: {self.ra})"
    
class Laudo(models.Model):
    descricao = models.CharField(max_length=250, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data do Laudo")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descricao} ({self.data.strftime('%d/%m/%Y')})"
    

class Interacoes(models.Model):
    data = models.DateField(verbose_name="Data")
    descricao = models.TextField(verbose_name="Descrição")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Interação em {self.data.strftime('%d/%m/%Y')} - {self.aluno.nome}"


class Indicativo(models.Model):
    descricao = models.CharField(max_length=250, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    indicativo = models.BooleanField(verbose_name="Indicativo")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descricao} ({self.data.strftime('%d/%m/%Y')})"
    
class Intervencao(models.Model):
    data = models.DateField(verbose_name="Data")
    descricao = models.TextField(verbose_name="Descrição")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Intervenção em {self.data.strftime('%d/%m/%Y')} - {self.aluno.nome}"
    

class Pte(models.Model):
    data_criacao = models.DateField(verbose_name="Data de Criação")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="ptes")
    # Já existem em outras classes: curso/serie -> vêm de aluno.curso (e disciplina.curso)
    ano_letivo = models.PositiveIntegerField(verbose_name="Ano Letivo", null=True, blank=True)

    # Dados do componente curricular
    componente_curricular = models.ForeignKey( Disciplina, on_delete=models.SET_NULL, verbose_name="Componente Curricular", null=True, blank=True)
    # Mantém para permitir indicar o professor específico do PTE
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.SET_NULL, verbose_name="Professor(a) Responsável", null=True, blank=True)
    periodo_inicio = models.DateField(verbose_name="Início do PTE", null=True, blank=True)
    periodo_fim = models.DateField(verbose_name="Fim do PTE", null=True, blank=True)

    # Registros do PTE
    potencialidades_dificuldades_habilidades = models.TextField(verbose_name="Potencialidades, dificuldades e habilidades do estudante", null=True, blank=True)
    recursos_servicos_procedimentos = models.TextField(verbose_name="Recursos, serviços e procedimentos necessários para adaptação", null=True, blank=True)
    expectativas_aprendizagem = models.TextField(verbose_name="Expectativas de aprendizagem pretendidas", null=True, blank=True)
    conteudos_previstos = models.TextField(verbose_name="Conteúdos previstos", null=True, blank=True)
    instrumentos_avaliativos = models.TextField(verbose_name="Instrumentos avaliativos previstos para adaptação", null=True, blank=True)
    anexos = models.TextField(verbose_name="Anexos", null=True, blank=True)
    informacoes_adicionais = models.TextField(verbose_name="Informações adicionais", null=True, blank=True)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    # Deriva curso e série a partir das relações já existentes
    @property
    def curso(self):
        if self.aluno and getattr(self.aluno, "curso_id", None):
            return self.aluno.curso
        if self.componente_curricular and getattr(self.componente_curricular, "curso_id", None):
            return self.componente_curricular.curso
        return None

    @property
    def serie(self):
        c = self.curso
        return getattr(c, "serie", None) if c else None

    def clean(self):
        errors = {}

        # Garante coerência entre aluno.curso e disciplina.curso
        if (
            self.componente_curricular
            and self.aluno
            and getattr(self.aluno, "curso_id", None)
            and getattr(self.componente_curricular, "curso_id", None)
            and self.aluno.curso_id != self.componente_curricular.curso_id
        ):
            errors["componente_curricular"] = "A disciplina não pertence ao mesmo curso do aluno."

        # Garante que o professor está vinculado à disciplina selecionada
        if (
            self.professor_responsavel
            and self.componente_curricular
            and self.professor_responsavel.disciplina_id != self.componente_curricular_id
        ):
            errors["professor_responsavel"] = "O professor precisa estar vinculado à disciplina selecionada."

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        comp = self.componente_curricular.nome if self.componente_curricular else "Sem componente"
        return f"PTE de {self.aluno.nome} - {comp} ({self.data_criacao.strftime('%d/%m/%Y')})"
    
class RelatorioPte(models.Model):
    pte = models.OneToOneField(Pte, on_delete=models.CASCADE, related_name="relatorio", verbose_name="PTE")
    data = models.DateField(verbose_name="Data do Relatório")
    
     # Relatório do PTE
    rel_expectativas_nao_alcancadas = models.TextField(verbose_name="Expectativas de aprendizagem não alcançadas", null=True, blank=True)
    rel_conteudos_nao_alcancados = models.TextField(verbose_name="Conteúdos não alcançados", null=True, blank=True)
    rel_avaliacao_recursos_adaptados = models.TextField(verbose_name="Avaliação da aplicação dos recursos adaptados", null=True, blank=True)
    rel_aspectos_desempenho = models.TextField(verbose_name="Aspectos observados quanto ao desempenho do estudante", null=True, blank=True)
    rel_dificuldades_professor = models.TextField(verbose_name="Dificuldades encontradas pelo professor", null=True, blank=True)
    rel_anexos = models.TextField(verbose_name="Anexos (Relatório)", null=True, blank=True)
    rel_informacoes_adicionais = models.TextField(verbose_name="Informações adicionais (Relatório)", null=True, blank=True)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Relatório do PTE de {self.pte.aluno.nome} em {self.data.strftime('%d/%m/%Y')}"