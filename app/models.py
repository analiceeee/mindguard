from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):  # herdando do User do Django
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tipo = models.CharField(max_length=12, choices=[('aluno', 'Aluno'), ('profissional', 'Profissional')])

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)
    curso = models.CharField(max_length=100)
    turma = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.usuario.nome} - {self.matricula}'


class Profissional(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.usuario.nome} - {self.especialidade}'


class Questionario(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    TIPOS = [
        ('escala', 'Escala'),
        ('texto', 'Texto Aberto'),
    ]

    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPOS)

    def __str__(self):
        return self.texto


class Resposta(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    resposta_texto = models.TextField(null=True, blank=True)
    resposta_numerica = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if self.resposta_numerica is not None:
            return f'{self.aluno.usuario.nome} - {self.pergunta.texto}: {self.resposta_numerica}'
        return f'{self.aluno.usuario.nome} - {self.pergunta.texto}: {self.resposta_texto}'


class DiarioEmocional(models.Model):
    HUMORES = [
        ('feliz', 'Feliz'),
        ('triste', 'Triste'),
        ('ansioso', 'Ansioso'),
        ('calmo', 'Calmo'),
        ('outro', 'Outro'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    humor = models.CharField(max_length=50, choices=HUMORES)

    def __str__(self):
        return f'{self.aluno.usuario.nome} - {self.titulo}'


class Encaminhamento(models.Model):
    STATUS = [
        ('pendente', 'Pendente'),
        ('realizado', 'Realizado'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    motivo = models.TextField()
    data_encaminhamento = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f'Encaminhamento de {self.aluno.usuario.nome} para {self.profissional.usuario.nome} - {self.status}'


class RecursoEducacional(models.Model):
    TIPOS = [
        ('video', 'Vídeo'),
        ('artigo', 'Artigo'),
        ('podcast', 'Podcast'),
    ]

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    url = models.URLField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
