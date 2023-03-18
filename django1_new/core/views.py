from django.shortcuts import render
from .models import Produto

# Create your views here.

def index(request):
    
    if str(request.user) == 'AnonymousUser':
        logado = 'Usuário não logado!'
    else:
        logado = 'Usuário ' + str(request.user) + ' logado!'

    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'logado' : logado,
        'produtos' : produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    produto_sel = Produto.objects.get(id = pk)
    context = {
        'produto' : produto_sel
    }
    return render(request, 'produto.html', context)