from django.shortcuts import render
from django.views import View
from .models import Questionario, RecursoEducacional, DiarioEmocional

class IndexView(View):
    def get(self, request, *args, **kwargs):
        questionarios = Questionario.objects.all().order_by('-criado_em')[:5]
        recursos = RecursoEducacional.objects.all()[:5]
        diarios = DiarioEmocional.objects.all().order_by('-data')[:5]

        context = {
            'questionarios': questionarios,
            'recursos': recursos,
            'diarios': diarios,
        }

        return render(request, 'index.html', context)

    def post(self, request):
        # Por enquanto, não há formulário a tratar
        pass
