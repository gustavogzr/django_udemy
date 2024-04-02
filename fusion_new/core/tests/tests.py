from django.test import TestCase

# Create your tests here.
def add_num(num):
    return num + 1 

class SimplesTesteCase(TestCase): # toda classe de teste deve herdar de TestCase

    def setUp(self): # roda antes de cada teste
        self.numero = 41

    def test_add_num(self): # esta função realiza o teste da função add_num
        # todo teste deve começar com a palavra test_
        valor = add_num(self.numero)
        self.assertTrue(valor == 42) # verifica se o valor retornado é 42

    def test_add_num_erro_proposital(self): # esta função irá falhar propositalmente
        valor = add_num(self.numero)
        self.assertTrue(valor == 43)

