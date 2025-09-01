from django.contrib import admin
from .models import (
    Usuario, Aluno, Profissional,
    Questionario, Pergunta, Resposta,
    DiarioEmocional, Encaminhamento, RecursoEducacional
)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'nome', 'email', 'tipo')
    search_fields = ('username', 'nome', 'email')
    list_filter = ('tipo',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'matricula', 'curso', 'turma')
    search_fields = ('usuario__nome', 'matricula', 'curso', 'turma')

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'especialidade')
    search_fields = ('usuario__nome', 'especialidade')

@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado_em')
    search_fields = ('nome',)

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'tipo', 'questionario')
    list_filter = ('tipo',)
    search_fields = ('texto',)

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'pergunta', 'data')
    search_fields = ('aluno__usuario__nome', 'pergunta__texto')

@admin.register(DiarioEmocional)
class DiarioEmocionalAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'titulo', 'data', 'humor')
    list_filter = ('humor',)
    search_fields = ('aluno__usuario__nome', 'titulo')

@admin.register(Encaminhamento)
class EncaminhamentoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'profissional', 'data_encaminhamento', 'status')
    list_filter = ('status',)
    search_fields = ('aluno__usuario__nome', 'profissional__usuario__nome')

@admin.register(RecursoEducacional)
class RecursoEducacionalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'url')
    list_filter = ('tipo',)
    search_fields = ('titulo',)
