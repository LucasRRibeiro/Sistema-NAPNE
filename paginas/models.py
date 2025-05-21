from django.db import models

#OBS: quando tivermos um objeto de uma outra classe, teremos um chave estrangeira e vamos
#Utilizar models.ForeignKey(Classe do objeto, on_delete=model.PROTECT ou Cascate (o on_delete vai depender da minha situação, se pode ou não deletar um campo na classe do objeto))

#O tipo de dado inteiro vária em várias opções com Positive, small, big. Com parametros para sua forma de iniciar(default=0)

# Todas as classes DEVEM ter herança de models.Model
# Create your models here.

#Crie suas classes
class Laudo(models.Model):
    #Definir os atributos
    descricao = models.CharField(max_length=250, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data do Laudo")

    def __str__(self):
     return f"{self.descricao} ({self.data.strftime('%d/%m/%Y')})"

class Napne(models.Model):
    #Definir os atributos
   data_criacao = models.DateField(verbose_name="Data de Criação")
   descricao = models.CharField(max_length=250, verbose_name="Descrição")

   def __str__(self):
     return f"{self.descricao} ({self.data_criacao.strftime('%d/%m/%Y')})"

class Responsavel(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    fone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(verbose_name="E-mail")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")

    def __str__(self):
     return self.nome
class Indicativo(models.Model):
    descricao = models.CharField(max_length=250, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    indicativo = models.BooleanField(verbose_name="Indicativo")

    def __str__(self):
     return f"{self.descricao} ({self.data.strftime('%d/%m/%Y')})"
class Aluno(models.Model):
    ra = models.PositiveIntegerField(unique=True, verbose_name="RA")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    fone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(verbose_name="E-mail")
    curso = models.CharField(max_length=100, verbose_name="Curso")
    ano = models.PositiveSmallIntegerField(verbose_name="Ano")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    rg = models.CharField(max_length=20, verbose_name="RG")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    laudo = models.ForeignKey(Laudo, on_delete=models.PROTECT, verbose_name="Laudo", null=True, blank=True)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.SET_NULL, verbose_name="Responsável", null=True, blank=True)

    def __str__(self):
     return f"{self.nome} (RA: {self.ra})"

class Interacoes(models.Model):
    data = models.DateField(verbose_name="Data")
    descricao = models.TextField(verbose_name="Descrição")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name="Aluno")

    def __str__(self):
     return f"Interação em {self.data.strftime('%d/%m/%Y')} - {self.aluno.nome}"
    
class Servidor(models.Model):
    siape = models.PositiveIntegerField(unique=True, verbose_name="SIAPE")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    fone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(verbose_name="E-mail")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    tipo = models.CharField(max_length=50, verbose_name="Tipo")
    napne = models.ForeignKey(Napne, on_delete=models.CASCADE, verbose_name="NAPNE")

    def __str__(self):
     return f"{self.nome} (SIAPE: {self.siape})"