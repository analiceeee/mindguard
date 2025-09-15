# app/admin.py

from django.contrib import admin
from .models import Pessoa, Ocupacao, Questionario, Pergunta, Resposta, DiarioEmocional, Encaminhamento, RecursoEducacional

# Inline para Perguntas dentro de Questionário
class PerguntaInline(admin.TabularInline):
    model = Pergunta
    extra = 1
    fields = ('texto',)

# Inline para Respostas
class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 0
    fields = ('pessoa', 'pergunta', 'resposta_texto', 'data')
    readonly_fields = ('data',)

# Inline para Diários
class DiarioEmocionalInline(admin.TabularInline):
    model = DiarioEmocional
    extra = 0
    fields = ('titulo', 'conteudo', 'humor', 'data')
    readonly_fields = ('data',)

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'ocupacao')
    search_fields = ('username', 'email')
    list_filter = ('ocupacao',)

@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado_em')
    search_fields = ('nome',)
    inlines = [PerguntaInline]

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'questionario')
    list_filter = ('questionario',)
    search_fields = ('texto',)

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'pergunta', 'resposta_texto_preview', 'data')
    list_filter = ('pessoa', 'pergunta__questionario', 'data')
    search_fields = ('pessoa__username', 'pergunta__texto')
    readonly_fields = ('data',)

    def resposta_texto_preview(self, obj):
        return (obj.resposta_texto[:50] + '...') if obj.resposta_texto and len(obj.resposta_texto) > 50 else obj.resposta_texto
    resposta_texto_preview.short_description = 'Resposta'

@admin.register(DiarioEmocional)
class DiarioEmocionalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pessoa', 'humor', 'data')
    search_fields = ('titulo', 'pessoa__username')
    list_filter = ('humor', 'data')

@admin.register(Encaminhamento)
class EncaminhamentoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'ocupacao', 'data_encaminhamento')
    list_filter = ('ocupacao', 'data_encaminhamento')
    search_fields = ('pessoa__username', 'motivo')

@admin.register(RecursoEducacional)
class RecursoEducacionalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'url')
    search_fields = ('titulo', 'tipo')