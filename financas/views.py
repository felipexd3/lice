"""
módulo para renderização de páginas html,
respostas nas paginas http e formularios receitas e despesas
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .forms import ReceitasForm, DespesasForm
from .models import Receitas, Despesas




def nova_receita(request):
    """
    se post, irá persistir o que estiver no formulário no bd
    se get, irá renderizar um formulário em branco para preenchimento
    """
    if request.method == 'POST':
        form = ReceitasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Sucessso!')
    else:
        form = ReceitasForm()
    return render(request, 'financas/nova_receita.html', {'form': form})

def nova_despesa(request):
    """
    se post, irá persistir o que estiver no formulário no bd
    se get, irá renderizar um formulário em branco para preenchimento
    """
    if request.method == 'POST':
        form = DespesasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Sucesso!')
    else:
        form = DespesasForm()
    return render(request, 'financas/nova_despesa.html', {'form': form})


def home(request):
    """
    objetos pagina principal
    """
    receitas = Receitas.objects.aggregate(Sum('valor'))
    total_receitas = receitas['valor__sum']
    despesas = Despesas.objects.aggregate(Sum('valor'))
    total_despesas = despesas['valor__sum']

    receitas = receitas['valor__sum']
    despesas = despesas['valor__sum']

    total = total_receitas - total_despesas

    lista_receitas = Receitas.objects.all()

    lista_despesas = Despesas.objects.all()

    dados = {
        'total': total, 'receitas': receitas, 'despesas': despesas, 'lista_receitas': lista_receitas, 'lista_despesas': lista_despesas
    }

    return render(request, 'financas/home.html', {'dados': dados})
