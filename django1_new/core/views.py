from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
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
    #produto_sel = Produto.objects.get(id = pk)
    produto_sel = get_object_or_404(Produto, id = pk)
    context = {
        'produto' : produto_sel
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)