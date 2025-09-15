# app/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# RF02: Ocupação
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

# RF01: Pessoa
class Pessoa(AbstractUser):
    email = models.EmailField(unique=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.username} ({self.ocupacao or 'Sem ocupação'})"

# RF04: Questionário
class Questionario(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)  # RF04
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# RF05: Pergunta
class Pergunta(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.texto

# RF06: Resposta — vinculada à Pessoa
class Resposta(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)  # RF06
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta_texto = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pessoa.username} - {self.pergunta.texto}"

# RF07: Diário Emocional — vinculado à Pessoa
class DiarioEmocional(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)  # RF07
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()  # RF07
    humor = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.pessoa.username}"

# RF08: Encaminhamento
class Encaminhamento(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)  # RF08
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)  # RF08
    motivo = models.TextField()
    data_encaminhamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Encaminhamento de {self.pessoa.username} para {self.ocupacao.nome}"

# RF09: Recurso Educacional
class RecursoEducacional(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)  # RF09
    tipo = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.titulo