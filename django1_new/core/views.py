from django.shortcuts import render

# Create your views here.

def index(request):
    
    if str(request.user) == 'AnonymousUser':
        logado = 'Usuário não logado!'
    else:
        logado = 'Usuário ' + str(request.user) + ' logado!'

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'logado' : logado
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')