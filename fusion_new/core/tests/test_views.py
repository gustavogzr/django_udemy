from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.views import IndexView

class IndexViewTestCase(TestCase):

        def setUp(self):
            self.dados = {
                'nome': 'Felicity Jones',
                'email': 'felicity@gmail.com',
                'assunto': 'Um assunto qualquer',
                'mensagem': 'Uma mensagem qualquer'
            }
            self.cliente = Client()

        def test_form_valid(self):
            request = self.cliente.post(reverse_lazy('index'), data=self.dados)
            self.assertEquals(request.status_code, 302) # 302 = Redirecionamento temporário

        def test_form_invalid(self):
            dados = {
                'nome': 'Felicity Jones',
                'assunto': 'Um assunto qualquer'
            }
            request = self.cliente.post(reverse_lazy('index'), data=dados)
            self.assertEquals(request.status_code, 200)

