from django.contrib.auth.models import User
from django.db import models


class Napne(models.Model):
    data_criacao = models.DateField(verbose_name="Data de Criação")
    descricao = models.CharField(max_length=250, verbose_name="Descrição")

    def __str__(self):
        return f"{self.descricao} ({self.data_criacao.strftime('%d/%m/%Y')})"
    

class Servidor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='servidor')
    siape = models.PositiveIntegerField(unique=True, verbose_name="SIAPE")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    fone = models.CharField(max_length=15, verbose_name="Telefone")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    tipo = models.CharField(max_length=50, verbose_name="Tipo")
    napne = models.ForeignKey(Napne, on_delete=models.CASCADE, verbose_name="NAPNE")

    def __str__(self):
        return f"{self.nome} (SIAPE: {self.siape})"


class Responsavel(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='responsavel')
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    fone = models.CharField(max_length=15, verbose_name="Telefone")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')
    ra = models.PositiveIntegerField(unique=True, verbose_name="RA")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    fone = models.CharField(max_length=15, verbose_name="Telefone")
    curso = models.CharField(max_length=100, verbose_name="Curso")
    ano = models.PositiveSmallIntegerField(verbose_name="Ano")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    rg = models.CharField(max_length=20, verbose_name="RG")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    responsavel = models.ForeignKey(Responsavel, on_delete=models.SET_NULL, verbose_name="Responsável", null=True, blank=True)

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
    laudo = models.ForeignKey(Laudo, on_delete=models.CASCADE)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Interação em {self.data.strftime('%d/%m/%Y')} - {self.aluno.nome}"


class Indicativo(models.Model):
    descricao = models.CharField(max_length=250, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    indicativo = models.BooleanField(verbose_name="Indicativo")
    laudo = models.ForeignKey(Laudo, on_delete=models.CASCADE)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descricao} ({self.data.strftime('%d/%m/%Y')})"