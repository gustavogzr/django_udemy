from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _ # importação para tradução
from django.utils import translation # importação para tradução dinâmica

from .models import Servico, Funcionario, Recurso
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language() # obtém a linguagem atual
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = Recurso.objects.order_by('?').all()
        context['half_recursos'] = round(len(context['recursos']) / 2)
        context['lang'] = lang  # adiciona a linguagem ao contexto
        translation.activate(lang)  # ativa a linguagem atual
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso!')) # mensagem traduzida
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar e-mail!')) # mensagem traduzida
        return super(IndexView, self).form_invalid(form, *args, **kwargs)