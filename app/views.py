# app/views.py

from django.shortcuts import render
from django.views import View
from .models import Questionario, RecursoEducacional, DiarioEmocional, Pessoa, Pergunta, Resposta, Ocupacao, Encaminhamento

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

def pessoa_list(request):
    pessoas = Pessoa.objects.select_related('ocupacao').all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})

def ocupacao(request):
    ocupacoes = Ocupacao.objects.all()
    return render(request, "ocupacao.html", {'ocupacoes': ocupacoes})

def questionarios(request):
    questionarios = Questionario.objects.prefetch_related('perguntas').all().order_by('-criado_em')
    return render(request, "questionarios.html", {'questionarios': questionarios})

def perguntas(request):
    perguntas = Pergunta.objects.select_related('questionario').all()
    return render(request, "perguntas.html", {'perguntas': perguntas})

def respostas(request):
    respostas = Resposta.objects.select_related('pessoa', 'pergunta__questionario').all().order_by('-data')
    return render(request, "respostas.html", {'respostas': respostas})

def diarioemocional(request):
    diarios = DiarioEmocional.objects.select_related('pessoa').all().order_by('-data')
    return render(request, "diarioemocional.html", {'diarios': diarios})

def encaminhamento(request):
    encaminhamentos = Encaminhamento.objects.select_related('pessoa', 'ocupacao').all().order_by('-data_encaminhamento')
    return render(request, "encaminhamento.html", {'encaminhamentos': encaminhamentos})

def recursoseducacionais(request):
    recursos = RecursoEducacional.objects.all()
    return render(request, "recursoseducacionais.html", {'recursos': recursos})