# config/urls.py

from django.contrib import admin
from django.urls import path
from app.views import IndexView, pessoa_list, ocupacao, questionarios, perguntas, respostas, diarioemocional, encaminhamento, recursoseducacionais

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoa/', pessoa_list, name='pessoa_list'),
    path('ocupacao/', ocupacao, name='ocupacao'),
    path('questionarios/', questionarios, name='questionarios'),
    path('perguntas/', perguntas, name='perguntas'),
    path('respostas/', respostas, name='respostas'),
    path('diarioemocional/', diarioemocional, name='diarioemocional'),
    path('encaminhamento/', encaminhamento, name='encaminhamento'),
    path('recursoseducacionais/', recursoseducacionais, name='recursoseducacionais'),
]